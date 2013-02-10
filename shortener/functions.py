from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from urlparse import urlparse

def validate_url(_url):
	new_url = _url
	validate = URLValidator(verify_exists=False)
	parsed = urlparse(new_url)
	if not parsed.scheme:
		new_url = 'http://' + new_url

	try:
		validate(new_url)
		return new_url
	except ValidationError, e:
		return None

def base10ton(number, n):
	x = []
	while(number != 0):
		x.insert(0,number%n)
		number /= n

	if x:
		return x
	else:
		return [0]

def basento10(number, n):
	i = 0
	for elem in number:
		if elem != 0:
			break
		else:
			i+= 1
	
	solution = 0
	for x in range(i,len(number)):
		solution += number[x] * (n**(len(number)-x-1))

	return solution

def populate(array, n, k=0):
	return [k]*(n - len(array)) + array

def encode(number):
	f = open(settings.ALPHABET)
	alphabet = f.readline()
	f.close()

	a = populate(base10ton(number,len(alphabet)),4)
	return ''.join([alphabet[i] for i in a])

def decode(encoded):
	f = open(settings.ALPHABET)
	alphabet = f.readline()
	f.close()

	basen = [alphabet.index(i) for i in encoded]
	return basento10(basen,len(alphabet))
