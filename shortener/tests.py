"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

"""

from django.test import TestCase
from django.test.client import Client
from models import master
from functions import validate_url, base10ton, populate, basento10, encode, decode
from random import randint

class ViewsTest(TestCase):
	def test_home(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code,200)

class FunctionsTest(TestCase):
    def test_validate_url(self):
        self.assertEqual(validate_url('http://url.com'),'http://url.com')
        self.assertEqual(validate_url('http://www.url.com'),'http://www.url.com')
        self.assertEqual(validate_url('http://url.'),None)
        self.assertEqual(validate_url('http://url.url.com'),'http://url.url.com')
        self.assertEqual(validate_url('http://sub1.sub2.url.com'),'http://sub1.sub2.url.com')
        self.assertEqual(validate_url('http://url.com/path/to/some/folder'),'http://url.com/path/to/some/folder')
        self.assertEqual(validate_url('http://url.com/path/to/some/folder/'),'http://url.com/path/to/some/folder/')
        self.assertEqual(validate_url('http://url.com/?param1'),'http://url.com/?param1')
        self.assertEqual(validate_url('http://url.com/?param1=1'),'http://url.com/?param1=1')
        self.assertEqual(validate_url('http://url.com/?param1=something'),'http://url.com/?param1=something')
        self.assertEqual(validate_url('https://newprotocol.com/'),'https://newprotocol.com/')
        self.assertEqual(validate_url('ftp://newprotocol.com/'),'ftp://newprotocol.com/')
        self.assertEqual(validate_url('https://www.google.com.pe/search?q=url+validation+examples&oq=url+validation+examples&aqs=chrome.0.57j61j0j60l3.3437&sourceid=chrome&ie=UTF-8'),'https://www.google.com.pe/search?q=url+validation+examples&oq=url+validation+examples&aqs=chrome.0.57j61j0j60l3.3437&sourceid=chrome&ie=UTF-8')
        
        # Tests without protocol ...
        self.assertEqual(validate_url('url.com'),'http://url.com')
        self.assertEqual(validate_url('www.url.com'),'http://www.url.com')
        self.assertEqual(validate_url('url.'),None)
        self.assertEqual(validate_url('url.url.com'),'http://url.url.com')
        self.assertEqual(validate_url('sub1.sub2.url.com'),'http://sub1.sub2.url.com')
        self.assertEqual(validate_url('url.com/path/to/some/folder'),'http://url.com/path/to/some/folder')
        self.assertEqual(validate_url('url.com/path/to/some/folder/'),'http://url.com/path/to/some/folder/')
        self.assertEqual(validate_url('url.com/?param1'),'http://url.com/?param1')
        self.assertEqual(validate_url('url.com/?param1=1'),'http://url.com/?param1=1')
        self.assertEqual(validate_url('url.com/?param1=something'),'http://url.com/?param1=something')
        self.assertEqual(validate_url('newprotocol.com/'),'http://newprotocol.com/')
        self.assertEqual(validate_url('ftp:/newprotocol.com/'),None)
        self.assertEqual(validate_url('https:/www.google.com.pe/search?q=url+validation+examples&oq=url+validation+examples&aqs=chrome.0.57j61j0j60l3.3437&sourceid=chrome&ie=UTF-8'),None)

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
        # if the number to populate is lower than the array?
        self.assertEqual(populate([0,1,2,3,4,5],5,3), [0,1,2,3,4,5])
        self.assertEqual(populate([0,1,2,3,4,5],2,3), [0,1,2,3,4,5])
        self.assertEqual(populate([0,1,2,3,4,5],3), [0,1,2,3,4,5])


    def test_basento10(self):
        self.assertEqual(basento10([0,1],2), 1)
        self.assertEqual(basento10([0,0],2), 0)
        self.assertEqual(basento10([1,0,0,0],2), 8)
        self.assertEqual(basento10([0,0],2412321), 0)
        self.assertEqual(basento10([10],11), 10)
        self.assertEqual(basento10([1,0],11), 11)
        self.assertEqual(basento10([1,1],12), 13)

    def test_encode_decode(self):
        for i in range(0, 1234567, randint(20,100)):
            self.assertEqual(decode(encode(i)),i)