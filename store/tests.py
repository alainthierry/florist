from django.test import TestCase
from django.urls import reverse

class Vehicles(object):
    '''
    The Vehicle object contains a lot of vehicles

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    '''
    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance,destination):
        '''We can't travel distance in vehicles without fuels, so here is the fuels

        Args:
            distance (int): The amount of distance traveled
            destination (bool): Should the fuels refilled to cover the distance?

        Raises:
            RuntimeError: Out of fuel

        Returns:
            cars: A car mileage
        '''
        pass

class IndexPageTestCase(TestCase):
	"""docstring for IndexPageTestCase

	The IndexPageTestCase object is to test page return status,

	"""
	
	def test_inddex_page(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)

class SearchViewTestCase(TestCase):
	"""docstring for SearchViewTestCase"""
	def test_search_view(self):
		response = self.client.get(reverse('store:search'))
		self.assertEqual(response.status_code, 200)
		