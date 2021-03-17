from django.contrib import admin
from store.models import (
	Customer, Booking, Flower
)
""" Register models for admin """

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Flower)

