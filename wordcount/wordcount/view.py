from django.http import HttpResponse




def homepage (request):

	return HttpResponse('hello')

def eggs (request):

	return HttpResponse('<h1>EGGS</h1>')  