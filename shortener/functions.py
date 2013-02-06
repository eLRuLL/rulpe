from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from urlparse import urlparse

def validate_url(_url):
	validate = URLValidator(verify_exists=False)
	parsed = urlparse(_url)
	if not parsed.scheme:
		_url = 'http://' + _url

	try:
		validate(_url)
		return True
	except ValidationError, e:
		return False


def encode_url(_url):
	pass