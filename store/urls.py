from django.urls import path, re_path
from . import views


app_name = 'store'

urlpatterns = [
	re_path('', views.search, name='search'),
	
]