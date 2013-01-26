# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from random import randint
from models import Paginas
from datetime import datetime

def home(request):

	Pages = Paginas.objects.all().order_by('creation_time')
	lista = []
	for i in Pages:
		if len(str(i.long_url)) > 30:
			lista.append({'long_url': str(i.long_url)[:30] + '...','short_url': i.short_url, 'creation_time':i.creation_time, 'clicks':i.clicks})
		else:
			lista.append({'long_url': str(i.long_url),'short_url': i.short_url, 'creation_time':i.creation_time, 'clicks':i.clicks})
	return render(request,'../templates/index.html',{'Pages': lista})


def shortener(request):
	alfa = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	myurl = request.GET.get('the_url',None)
	if myurl.strip() == "":
		return redirect('home')
	else:
		if Paginas.objects.filter(long_url=myurl).exists():
			temp_short = Paginas.objects.get(long_url=myurl)
			return render(request, '../templates/yaexiste.html',{'shorten' : temp_short.short_url})
		else:
			short_url = ''
			for i in xrange(5):
				short_url += alfa[randint(0,len(alfa)-1)]

			tries = 0
			while Paginas.objects.filter(short_url=short_url).exists():
				# Paginas.objects.get(short_url=short_url)
				short_url = ''
				for i in xrange(5):
					short_url += alfa[randint(0,len(alfa)-1)]
				tries += 1
				print str(tries) + " , short_url:" + short_url

			my_page = Paginas(short_url=short_url, long_url=myurl, creation_time=datetime.now(),clicks=0)
			my_page.save()

		return render(request, '../templates/shortener.html',{'myurl':myurl})

def counter(request,cosa):
	temp_short = Paginas.objects.get(short_url=cosa)
	temp_short.clicks += 1
	temp_short.save()
	return redirect('http://' + temp_short.long_url)