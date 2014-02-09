# Create your views here.
from datetime import datetime

from django.http import Http404
from django.shortcuts import redirect, render

from models import Master
from rulpe.apps.shortener.functions import validate_url, encode, decode


def home(request):
    # First, we need to define how are we gonna show the list. (which order)
    pages = Master.objects.all().order_by('creation_time')
    lista = []
    for i in pages:
        if len(str(i.long_url)) > 30:
            lista.append(
                {
                    'long_url': str(i.long_url)[:30] + '...',
                    'short_url': i.short_url,
                    'creation_time': i.creation_time,
                    'clicks': i.clicks
                }
            )
        else:
            lista.append(
                {
                    'long_url': str(i.long_url),
                    'short_url': i.short_url,
                    'creation_time': i.creation_time,
                    'clicks': i.clicks
                }
            )
    return render(request, 'index.html', {'Pages': lista})


def shortener(request):
    real_url = request.POST.get('long_url', '')

    long_url = validate_url(real_url)
    if not long_url:
        return render(request, 'url_validation_error.html', {'bad_url': real_url})

    elif Master.objects.filter(long_url=long_url).exists():
        temp_short = Master.objects.get(long_url=long_url)
        return render(request, 'exists.html', {'shorten': temp_short.short_url})

    else:

        record = Master(short_url='', long_url=long_url, creation_time=datetime.now(), clicks=0)
        record.save()

        # Unique Code Generator Function for SHORT_URL
        short_url = encode(record.id)

        Master.objects.filter(id=record.id).update(short_url=short_url)

        return render(request, 'shortener.html', {'long_url': long_url, 'short_url': short_url})


def counter(request, shorten):

    try:
        temp_short = Master.objects.get(id=decode(shorten))
    except:
        raise Http404()
    temp_short.clicks += 1
    temp_short.save()
    return redirect(temp_short.long_url)