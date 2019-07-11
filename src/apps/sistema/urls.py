from django.conf.urls import url, include
from apps.sistema.views import index,registrarproductos,listar_productos,listar_productos2,registrartarjetas

from django.urls import include, path

app_name = "sistema";

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevoproducto', registrarproductos,name='newprod'),
    url(r'^listarproductos', listar_productos,name='listaprod'),
    url(r'^lista_produc2(?P<id_producto>\d+)/$', listar_productos2, name='listaproducto2'),
    url(r'^tarjetas', registrartarjetas,name='newtarjet'),
]