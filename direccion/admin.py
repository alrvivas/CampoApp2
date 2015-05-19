from django.contrib import admin
from .models import Direccion, Estado,Ciudad

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre')

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre')

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
	list_display 	= ('id','calle','colonia',)