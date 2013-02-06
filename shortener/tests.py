"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import master
from functions import validate_url

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

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)