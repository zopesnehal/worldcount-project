from django.http import HttpResponse




def homepage (request):

	return HttpResponse('hello')

def eggs (request):

	return HttpResponse('eggs is greats')  