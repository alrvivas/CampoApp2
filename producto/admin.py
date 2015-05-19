from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display 	= ('id','categoria','name','stock','peso','precio_a','precio_b', 'orden')
	list_editable 	= ('stock','peso','precio_a','precio_b','orden',)
	list_filter 	= ('categoria',)


	prepopulated_fields = {'slug' : ('name',)} 