"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
import simplejson as json
from moodle2 import ORM

# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
	"""Tests for the application views."""
	# Django requires an explicit setup() when running tests in PTVS
	@classmethod
	def setUpClass(cls):
		django.setup()
		super(SimpleTest, cls).setUpClass()

	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		self.assertEqual(1 + 1, 2)
	def jsonTest(self):
		course1=ORM.user(1,"Kevinazo","teacher")
		json.dump(course1.__json__(),separators(',','"'),sort_keys=False)
		return course1.__str__()