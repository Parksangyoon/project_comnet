from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'start/startscreen.html')

def selectcharacter(request):
	return render(request, 'start/selectcharacter.html')

def selectcard(request):
	return render(request, 'start/selectcard.html')