"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import master

class ViewsTest(TestCase):
	def test_home(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code,200)


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        print 'hola'
        self.assertEqual(1 + 1, 2)