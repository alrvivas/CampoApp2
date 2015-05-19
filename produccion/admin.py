#encoding:utf-8
from django.contrib import admin
from models import ProduccionEsperada, ProduccionRealizada,ProduccionEsperadaCategoria

@admin.register(ProduccionEsperadaCategoria)
class ProduccionEsperadaCategoriaAdmin(admin.ModelAdmin):
	list_display 	= ('id','categoria','cantidad','fecha_cracion','fecha_a_agendar')
	list_editable 	= ('fecha_a_agendar',)

@admin.register(ProduccionEsperada)
class ProduccionEsperadaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_cracion','fecha_a_agendar')
	list_editable 	= ('fecha_a_agendar',)
	

@admin.register(ProduccionRealizada)
class ProduccionRealizadaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','cantidad_reproceso','fecha_de_elaboracion','fecha_cracion')
	list_editable 	= ('fecha_de_elaboracion','cantidad_reproceso',)
	list_filter 	= ('producto','fecha_de_elaboracion',)
	