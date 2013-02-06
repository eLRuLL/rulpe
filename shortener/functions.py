from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(_url):
	
	validate = URLValidator(verify_exists=False)
	try:
		validate(_url)
		return True
	except ValidationError, e:
	    return False