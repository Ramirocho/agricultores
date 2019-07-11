from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
	return render(request, 'agri/index.html')

def informacion(request):
	return render(request, 'agri/informacion.html')