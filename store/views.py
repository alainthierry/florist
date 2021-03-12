from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings


def index(request):
	context = {
		'page_title': 'La beauté dans les Fleurs',
		'title': 'Les Fleurs raconte une vie, Trouvez la vôtre',
	}
	return render(request, 'store/base.html', context)


def search(request):
	context = {
		'page_title': 'La beauté dans les Fleurs',
		'title': 'Les Fleurs Trouvées !',
	}
	query = request.GET.get('query')
	if query:
		print("found sthg \n"+query)
	else:
		print("We didn't find anything !")

	return render(request, 'store/base.html', context)
	"""
	subject = 'Thank you for registering to our site'
	message = ' it  means a world to us '
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ['cobayeleamire@gmail.com',]
	send_mail( subject, message, email_from, recipient_list )
	return redirect('redirect to a new page')"""