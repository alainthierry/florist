from django.urls import path, re_path
from . import views


app_name = 'store'

urlpatterns = [
	re_path(r'^search/', views.search, name='search'),
	
]