"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

"""

from django.test import TestCase
from django.test.client import Client
from models import master
from functions import validate_url, base10ton, populate

class ViewsTest(TestCase):
	def test_home(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code,200)

class FunctionsTest(TestCase):
    def test_validate_url(self):
        self.assertEqual(validate_url('http://url.com'),True)
        self.assertEqual(validate_url('http://www.url.com'),True)
        self.assertEqual(validate_url('http://url.'),False)
        self.assertEqual(validate_url('http://url.url.com'),True)
        self.assertEqual(validate_url('http://sub1.sub2.url.com'),True)
        self.assertEqual(validate_url('http://url.com/path/to/some/folder'),True)
        self.assertEqual(validate_url('http://url.com/path/to/some/folder/'),True)
        self.assertEqual(validate_url('http://url.com/?param1'),True)
        self.assertEqual(validate_url('http://url.com/?param1=1'),True)
        self.assertEqual(validate_url('http://url.com/?param1=something'),True)
        self.assertEqual(validate_url('https://newprotocol.com/'),True)
        self.assertEqual(validate_url('ftp://newprotocol.com/'),True)
        self.assertEqual(validate_url('https://www.google.com.pe/search?q=url+validation+examples&oq=url+validation+examples&aqs=chrome.0.57j61j0j60l3.3437&sourceid=chrome&ie=UTF-8'),True)
        
        # Tests without protocol ...
        self.assertEqual(validate_url('url.com'),True)
        self.assertEqual(validate_url('www.url.com'),True)
        self.assertEqual(validate_url('url.'),False)
        self.assertEqual(validate_url('url.url.com'),True)
        self.assertEqual(validate_url('sub1.sub2.url.com'),True)
        self.assertEqual(validate_url('url.com/path/to/some/folder'),True)
        self.assertEqual(validate_url('url.com/path/to/some/folder/'),True)
        self.assertEqual(validate_url('url.com/?param1'),True)
        self.assertEqual(validate_url('url.com/?param1=1'),True)
        self.assertEqual(validate_url('url.com/?param1=something'),True)
        self.assertEqual(validate_url('newprotocol.com/'),True)
        self.assertEqual(validate_url('ftp:/newprotocol.com/'),False)
        self.assertEqual(validate_url('https:/www.google.com.pe/search?q=url+validation+examples&oq=url+validation+examples&aqs=chrome.0.57j61j0j60l3.3437&sourceid=chrome&ie=UTF-8'),False)

    def test_base10ton(self):
        self.assertEqual(base10ton(0,2), [0])
        self.assertEqual(base10ton(0,132), [0])
        self.assertEqual(base10ton(1,2), [1])
        self.assertEqual(base10ton(1,1212), [1])
        self.assertEqual(base10ton(1,2), [1])
        self.assertEqual(base10ton(10,10), [1,0])
        self.assertEqual(base10ton(1234567890,10), [1,2,3,4,5,6,7,8,9,0])
        self.assertEqual(base10ton(62,62), [1,0])
        self.assertEqual(base10ton(3844,62), [1,0,0])
        self.assertEqual(base10ton(238328,62), [1,0,0,0])
        self.assertEqual(base10ton(14776336,62), [1,0,0,0,0])
        self.assertEqual(base10ton(14776335,62), [61,61,61,61])

    def test_populate(self):
        self.assertEqual(populate([],4), [0,0,0,0])
        self.assertEqual(populate([1],5), [0,0,0,0,1])
        self.assertEqual(populate([0,1,2,3,4,5],6), [0,1,2,3,4,5])
        self.assertEqual(populate([1],4,0), [0,0,0,1])
        self.assertEqual(populate([2],5,1), [1,1,1,1,2])
        self.assertEqual(populate([0,1,2],6,3), [3,3,3,0,1,2])
        self.assertEqual(populate([0,1,2,3,4,5],6,3), [0,1,2,3,4,5])