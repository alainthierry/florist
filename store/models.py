from django.db import models

""" ALL MODELS """

class Customer(models.Model):
	"""docstring for Customer
	This object represents the customer

	Attributes:
		name (str): The customer name,
		email(str) : The customer email,
		phone_number(str): The customer phone number,
	"""
	name = models.CharField("Nom", max_length=30)
	email = models.EmailField("Courrier électronique", unique=True)
	phone_number = models.CharField("Téléphone", max_length=20, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Client"
		verbose_name_plural  = "Clients"

class Booking(models.Model):
	"""docstring for Booking
	This object represents the booking

	Attributes:
		booked_date (Date): The booked date,
		delivery_date (Date): The delivery date,
		delivered (bool): Is the delivery done ?,
		customer (Customer): The customer who made the booking,

	"""
	booked_date = models.DateField("Date de réservation", auto_now_add=True)
	delivery_date = models.DateField("Date de livraison", )
	delivered = models.BooleanField("Livraison terminée", default=False)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	"""def __str__(self):
		return self.delivery_date
	"""

	class Meta:
		verbose_name = "Réservation"
		verbose_name_plural = "Réservations"

class Flower(models.Model):
	"""docstring for Flower
	This object reprents the flower that wil be booked

	Attributes:
		name (str): The name of the flower,
		description (str): The flower description,
		price (integer): The flower price,
		available (bool): Is the flower available ?,
		image_url(str): The flower image,
		booking (Booking): The Booking that contains the booked flower,
	"""
	name = models.CharField("Nom", max_length=30)
	description = models.TextField("Description")
	price = models.IntegerField("Prix", null=False)
	available = models.BooleanField(default=True)
	image_url = models.URLField("Image",)
	booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Fleur"
		verbose_name_plural = "Fleurs"
