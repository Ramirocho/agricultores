from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.sistema.models import registro,tarjetas
from apps.sistema.forms import RegistroDeProductos,CompraDeProductos,FormaPago
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template import RequestContext
# Create your views here.


@login_required	
def index(request):
	return render(request, 'agri/menu-principal.html')

@login_required
def registrarproductos(request):
	form = RegistroDeProductos(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = RegistroDeProductos()
	context = {
		'form': form,
	}
	return render(request, 'agri/registro-productos.html',context )

@login_required
def listar_productos(request):
	producto = registro.objects.all()
	contexto = {'productos':producto}
	return render(request,'agri/listar_productos.html',contexto)

@login_required
def listar_productos2(request, id_producto):
	producto = registro.objects.get(id = id_producto)
	tarjeta = tarjetas.objects.all()
	form = CompraDeProductos(request.POST)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = CompraDeProductos()

	contexto = {'productos2':producto,'form': form,'tarjetas':tarjeta}

	return render(request, 'agri/listar_productos2.html',contexto)


@login_required
def registrartarjetas(request):
	form = FormaPago(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = FormaPago()
	context = {
		'form': form,
	}
	return render(request, 'agri/registro-tarjetas.html',context )