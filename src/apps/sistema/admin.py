from django.contrib import admin
from apps.sistema.models import registro,compra,tarjetas

# Register your models here.
admin.site.register(registro)
admin.site.register(compra)
admin.site.register(tarjetas)