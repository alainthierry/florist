from django.contrib import admin
from store.models import (
	Customer, Booking, Flower
)
""" Register models for admin """


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_filter = ['name', 'email']
	list_display = ('name', 'email', 'phone_number')

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_filter = ['created_at',]
    list_display = ('name', 'description', 'price', 'available', 'image_url')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['delivered',]
    list_display = ('customer', 'flower', 'booked_date', 'delivered')
 




