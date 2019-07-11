from apps.usuarios.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.sistema.models import registro,compra,tarjetas


class RegistroDeProductos(forms.ModelForm):
	class Meta:
		model = registro

		fields = [
		'TipoFruVer',
		'FotoProducto',
		'NombreProducto',
		'CantidadKG',
		'Precio',
		'UsuarioName',
		'Usuario',
		'Latitud',
		'Longitud',
		]

		labels = {
		'TipoFruVer': 'Tipo de fruta o verdura',
		'FotoProducto': 'Foto del producto',
		'NombreProducto': 'Descripcion',
		'CantidadKG': 'Cantidad disponible (KG)',
		'Precio': 'Precio',
		'UsuarioName' : 'UsuarioName',
		'Usuario' : 'Usuario',
		'Latitud' : 'Latitud',
		'Longitud' : 'Longitud',
		}

		widgets = {
		'TipoFruVer': forms.Select(attrs={'class':'form-control'}),
		'FotoProducto': forms.FileInput(),
		'NombreProducto': forms.TextInput(attrs={'class':'form-control col-10'}),
		'CantidadKG': forms.TextInput(attrs={'class':'form-control col-10'}),
		'Precio': forms.TextInput(attrs={'class':'form-control col-10'}),
		'UsuarioName' : forms.TextInput(attrs={'class':'form-control col-10'}),
		'Usuario': forms.TextInput(attrs={'class':'form-control'}),
		'Latitud': forms.TextInput(attrs={'class':'form-control'}),
		'Longitud' : forms.TextInput(attrs={'class':'form-control'}),
		}


class CompraDeProductos(forms.ModelForm):
	class Meta:
		model = compra

		fields = [
		'idproducto',
		'cantidad',
		'valor',
		'vendedor',
		'comprador',
		'tipopago',
		]

		labels = {
		'idproducto' :'Id Producto',
		'cantidad' : 'Cantidad',
		'valor' : 'Valor',
		'vendedor' : 'Vendedor',
		'comprador' : 'Comprador',
		'tipopago' : 'tipo de pago',
		}

		widgets = {
		'idproducto': forms.TextInput(attrs={'class':'form-control col-10'}),
		'cantidad': forms.TextInput(attrs={'class':'form-control col-10'}),
		'valor': forms.TextInput(attrs={'class':'form-control col-10'}),
		'vendedor': forms.TextInput(attrs={'class':'form-control col-10'}),
		'comprador': forms.TextInput(attrs={'class':'form-control col-10'}),
		'tipopago' : forms.TextInput(attrs={'class':'form-control col-10'}),
		}


class FormaPago(forms.ModelForm):
	class Meta:
		model = tarjetas

		fields = [
		'idusuario',
		'tipotarjeta',
		'numero',
		'mesvencimiento',
		'añovencimiento',
		'cvc',
		]

		labels = {
		'idusuario': 'Id usuario',
		'tipotarjeta': 'Tipo de tarjeta',
		'numero': 'Numero de Cuenta',
		'mesvencimiento': 'Mes Vencimiento',
		'añovencimiento': 'Año Vencimiento',
		'cvc': 'CVC',
		}

		widgets = {
		'idusuario': forms.TextInput(attrs={'class':'form-control col-10'}),
		'tipotarjeta': forms.Select(attrs={'class':'form-control col-10'}),
		'numero': forms.TextInput(attrs={'class':'form-control col-10'}),
		'mesvencimiento': forms.Select(),
		'añovencimiento': forms.Select(),
		'cvc': forms.TextInput(attrs={'class':'form-control col-10'}),
		}