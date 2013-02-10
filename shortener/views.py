# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from random import randint
from models import master
from datetime import datetime
from functions import validate_url, populate, base10ton, encode, decode

def home(request):

	# First, we need to define how are we gonna show the list. (which order)
	Pages = master.objects.all().order_by('creation_time')
	lista = []
	for i in Pages:
		if len(str(i.long_url)) > 30:
			lista.append({'long_url': str(i.long_url)[:30] + '...','short_url': i.short_url, 'creation_time':i.creation_time, 'clicks':i.clicks})
		else:
			lista.append({'long_url': str(i.long_url),'short_url': i.short_url, 'creation_time':i.creation_time, 'clicks':i.clicks})
	return render(request,'index.html',{'Pages': lista})


def shortener(request):
	long_url = request.POST.get('long_url','')

	long_url = validate_url(long_url)
	if not long_url:
		return render(request,'url_validation_error.html',{'bad_url' : long_url})

	elif master.objects.filter(long_url=long_url).exists():
		temp_short = master.objects.get(long_url=long_url)
		return render(request,'exists.html',{'shorten' : temp_short.short_url})

	else:
		
		record = master(short_url='', long_url=long_url, creation_time=datetime.now(),clicks=0)
		record.save()

		# Unique Code Generator Function for SHORT_URL
		short_url = encode(record.id)

		master.objects.filter(id=record.id).update(short_url=short_url)

		return render(request,'shortener.html',{'long_url':long_url,'short_url':short_url})

def counter(request,shorten):

	temp_short = master.objects.get(id=decode(shorten))
	temp_short.clicks += 1
	temp_short.save()
	return redirect(temp_short.long_url)