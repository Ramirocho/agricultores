from django.db import models
from apps.usuarios.models import User

# Create your models here.


class registro(models.Model):

	Tipo = (('palta','palta'),('damasco','damasco'),('piña','piña'),('arándano','arándano'),('arándano (rojo)','arándano (rojo)'),
		('plátano','plátano'),('guinda','guinda'),('ciruela','ciruela'),('coco','coco'),('frambuesa','frambuesa'),('frutilla','frutilla'),
		('fresa','fresa'),('cereza','cereza'),('granada','granada'),('higo','higo'),('kiwi','kiwi'),('lima','lima'),('limón','limón'),
		('mandarina','mandarina'),('mango','mango'),('manzana','manzana'),('maracuyá','maracuyá'),('durazno','durazno'),('melón','melón'),
		('membrillo','membrillo'),('mora','mora'),('naranja','naranja'),('nectarina','nectarina'),('papaya','papaya'),('pera','pera'),
		('pomelo','pomelo'),('sandía','sandía'),('uva','uva'),(' zarzamora',' zarzamora'),
		('acelga','acelga'),('ajo','ajo'),('alcachofa','alcachofa'),('alcaucil','alcaucil'),('apio','apio'),('arveja','arveja'),
		('batata','batata'),('berenjena','berenjena'),('betarraga','betarraga'),('brócoli','brócoli'),('zapallo','zapallo'),('camote','camote'),
		('cebolla','cebolla'),('champiñón','champiñón'),('choclo','choclo'),('repollo','repollo'),('coles de Bruselas','coles de Bruselas'),
		('zapallo italiano','zapallo italiano'),('coliflor','coliflor'),('maíz','maíz'),('espárrago','espárrago'),('espinaca','espinaca'),
		('frijol','frijol'),('guisante','guisante'),('jitomate','jitomate'),('poroto','poroto'),('lechuga','lechuga'),
		('repollo morado','repollo morado'),('papa','papa'),('pepino','pepino'),('pimentón','pimentón'),('pimiento','pimiento'),('puerro','puerro'),
		('rábano','rábano'),('remolacha','remolacha'),('seta','seta'),('tomate','tomate'),('zanahoria','zanahoria'))
	TipoFruVer = models.CharField(max_length=50,choices=Tipo,default='papa')
	FotoProducto = models.FileField(upload_to="projects")	
	NombreProducto = models.CharField(max_length = 50)
	CantidadKG = models.IntegerField()
	Precio = models.IntegerField()
	UsuarioName = models.CharField(max_length = 50)
	Usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	Latitud = models.CharField(max_length=200)
	Longitud = models.CharField(max_length=200)


class compra(models.Model):
	idproducto = models.IntegerField()
	cantidad = models.IntegerField()
	valor = models.IntegerField()
	vendedor = models.CharField(max_length=200)
	comprador = models.CharField(max_length=200)
	tipopago = models.CharField(max_length=200)


class tarjetas(models.Model):
	idusuario = models.IntegerField()
	Tipos = (('Santander','Banco Santander'),('Banco BBVA','Banco BBVA'),('Banco de Chile','Banco de Chile'),('BancoEstado','BancoEstado'),('Banco Scotiabank','Banco Scotiabank'),
		('Banco Itau','Banco Itau'),('Banco Falabella','Banco Falabella'),('Visa','Visa'),('Mastercard','Mastercard'))
	tipotarjeta = models.CharField(max_length=50,choices=Tipos,default='Santander')
	numero = models.CharField(max_length = 16)
	Meses = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'))
	mesvencimiento = models.CharField(max_length = 99,choices=Meses,default='1')
	Años = (('2018','2018'),('2019','2019'),('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'))
	añovencimiento = models.CharField(max_length = 9999,choices=Años,default='2018')
	cvc = models.CharField(max_length = 3)