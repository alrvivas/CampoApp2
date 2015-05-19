from django.contrib import admin
from .models import TipoPago,Estatus,Orden,OrdenProducto

@admin.register(TipoPago)
class TipoPagoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)
	
@admin.register(Estatus)
class EstatusAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
	list_display 	= ('id','status','cliente','empleado','orden_total','orden_totalpeso','fecha_creacion')


@admin.register(OrdenProducto)
class OrdenProductoAdmin(admin.ModelAdmin):
	list_display 	= ('id','orden','producto','unit_price','cantidad','linea_subtotal','linea_subtotalpeso',)
	list_editable 	= ('cantidad','linea_subtotal','linea_subtotalpeso',)
	list_filter 	= ('orden',)
	search_fields = ('orden',)
