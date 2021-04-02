from django.shortcuts import render, get_object_or_404
from django.db import transaction, IntegrityError

from django.core.paginator import (
	Paginator, PageNotAnInteger, EmptyPage
)

from .models import (
	Flower, Booking, Customer
)	

from .forms import CustomerForm

def index(request):
	"""
	The home view that renders the main template
	
	Args:
		request (request): The request

    Returns:
    	(HttpResponse): The status_code of the  HttpResponse
	"""
	flowers = Flower.objects.filter(available=True).order_by('-created_at')[:6]
	context = {
		'page_title': 'La beauté dans les Fleurs',
		'title': 'Les Fleurs raconte une vie, Trouvez la vôtre',
		'flowers': flowers,
	}
	return render(request, 'store/list_flower.html', context)


def detail(request, flower_id):
	"""
	The home view that renders the main template
	
	Args:
		request (request): The request
		flower_id (integer): The flower id

    Returns:
    	(HttpResponse): The status_code of the  HttpResponse
	"""
	flower = get_object_or_404(Flower, pk=flower_id)
	context = {
		'page_title': flower.name,
		'title': flower.name,
		'flower': flower,
	}
	""" Handle booking step """
	if request.method == 'POST':
		form = CustomerForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			name = form.cleaned_data['name']
			phone_number = form.cleaned_data['phone_number']
			flower_id = form.cleaned_data['flower_id']

			try:
				with transaction.atomic():
					customer = Customer.objects.filter(email=email)
					if not customer.exists():
						customer = Customer.objects.create(
							email=email,
							name=name,
							phone_number=phone_number
						)
					else:
						customer = customer.first()
					flower = get_object_or_404(Flower, pk=flower_id)

					booking = Booking.objects.filter(flower=flower)
					if not booking.exists():
						booking = Booking.objects.create(
							customer=customer,
							flower=flower
						)
						flower.available = False
						flower.save()
						context = {
							'page_title': flower.name,
							'title': "Merci de nous faire confiance !",
						}
					else:
						context = {
							'page_title': flower.name,
							'title': "Merci de nous faire confiance !",

						}
						context['message'] = """
						Cette fleur n'est plus disponible dans le magasin. Veuillez choisir une 
						autre !
						"""
						return render(request, 'store/thank.html', context)
						
					return render(request, 'store/thank.html', context)

			except IntegrityError:
				form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."

	return render(request, 'store/detail.html', context)


def listing(request):
	"""
	The home view that renders the main template
	
	Args:
		request (request): The request

    Returns:
    	(HttpResponse): The status_code of the  HttpResponse
	"""
	flower_list = Flower.objects.filter(available=True)
	paginator = Paginator(flower_list, 6)
	page = request.GET.get('page')
	try:
		flowers = paginator.page(page)
	except PageNotAnInteger:
		flowers = paginator.page(1)
	except EmptyPage:
		flowers = paginator.page(paginator.num_pages)
	context = {
	'page_title': 'La beauté dans les Fleurs',
	'title': 'Toutes nos fleurs',
	'flowers': flowers
	}
	return render(request, 'store/listing.html', context)


def search(request):
	"""
	The home view that renders the main template
	
	Args:
		request (request): The request

    Returns:
    	(HttpResponse): The status_code of the  HttpResponse
	"""
	if request.method == 'GET':
		query = request.GET.get('query')
		context = {
			'page_title': 'La beauté dans les Fleurs',
			'query': query
		}
		if not query:
			flowers = Flower.objects.filter(available=True).order_by('-created_at')[:6]
		else:
			flowers = Flower.objects.filter(name__icontains=query, available=True)
		if not flowers.exists():
			flowers = Flower.objects.filter(description__icontains=query, available=True)
	else:
		flowers = Flower.objects.filter(available=True).order_by('-created_at')[:6]
		
	title = "Résultats pour la requête %s"%query
	context['flowers'] = flowers
	context['title'] = title

	return render(request, 'store/search_result.html', context)


def about(request):
	"""
	The home view that renders the main template
	
	Args:
		request (request): The request

    Returns:
    	(HttpResponse): The status_code of the  HttpResponse
	"""
	context = {
		'page_title': 'A propos de la La beauté dans les Fleurs',
		'title': 'A propos de nous !',
	}
	return render(request, 'store/about.html', context)