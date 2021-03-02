from django.shortcuts import render


def index(request):
	context = {
		'page_title': 'page_title',
		'title': 'title',
	}
	return render(request, 'base.html', context)