from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
	return HttpResponse("<h1>Hello and welcome back to your favorite Music App📻🎛️🎵</h1>")