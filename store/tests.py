from django.test import TestCase
from django.urls import reverse


class IndexPageTestCase(TestCase):
	"""docstring for IndexPageTestCase"""
	
	def test_inddex_page(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
