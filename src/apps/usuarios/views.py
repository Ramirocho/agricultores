from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuarios.models import User
from apps.usuarios.forms import RegistroForm
from django.urls import reverse_lazy
# Create your views here.



class RegistroUsuario(CreateView):
	model = User
	template_name = "agri/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('base:index')
