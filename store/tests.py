from django.test import TestCase
from django.urls import reverse

from .models import Flower, Customer, Booking


class IndexPageTestCase(TestCase):
	"""docstring for IndexPageTestCase

	The IndexPageTestCase object is to test page return status,

	"""
	
	def test_inddex_page(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)


class DetailPageTestCase(TestCase):

	def setUp(self):
		fleur = Flower.objects.create(
			name="Les fleurs",
			description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
			price=45.52,
			image_url="https://www.cdiscount.com/pdt2/1/1/6/1/700x700/neu8435300764116/rw/24-tetes-marguerite-bouquet-de-fleur-artificielle.jpg"
		)
		self.flower  = Flower.objects.get(name="Les fleurs")


	""" test that detail page returns a 200 if the item exists """
	def test_detail_page_returns_200(self):

		response = self.client.get(reverse('store:detail', args=(self.flower.id, )))
		self.assertEqual(response.status_code, 200)


	def test_detail_page_returns_404(self):

		response = self.client.get(reverse('store:detail', args=(self.flower.id+1, )))
		self.assertEqual(response.status_code, 404)


class BookingPageTestCase(TestCase):

	def setUp(self):
		fleur = Flower.objects.create(
			name="Les fleurs",
			description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
			price=45.52,
			image_url="https://www.cdiscount.com/pdt2/1/1/6/1/700x700/neu8435300764116/rw/24-tetes-marguerite-bouquet-de-fleur-artificielle.jpg"
		)

		customer = Customer.objects.create(
			email="thierry.iliho@um6p.ma",
			name="Alain Thierry",
			phone_number="212650038174"
		)

		self.flower = Flower.objects.get(name="Les fleurs")
		self.customer = Customer.objects.get(email="thierry.iliho@um6p.ma")

	""" test that a new booking is made """
	def test_new_booking_is_registered(self):
		customer = self.customer
		flower_id = self.flower.id
		old_bookings = Booking.objects.count()

		response = self.client.post(reverse('store:detail', args=(flower_id,)), {
			'email': customer.email,
			'name': customer.name,
			'phone_number': customer.phone_number,
			'flower_id': flower_id
		})
		new_bookings = Booking.objects.count()
		self.assertEqual(new_bookings, old_bookings + 1)

	""" test that a booking belongs to a customer """

	def test_new_booking_belongs_to_a_contact(self):
		customer = self.customer
		flower_id = self.flower.id

		response = self.client.post(reverse('store:detail', args=(flower_id,)), {
			'email': customer.email,
			'name': customer.name,
			'phone_number': customer.phone_number,
			'flower_id': flower_id
		})
		booking = Booking.objects.create(
			customer=self.customer,
			flower=self.flower
		)
		self.assertEqual(self.customer, booking.customer)






