from django.db import models

from producto.models import Product

class DevolucionBuena(models.Model):
	producto 			= models.ForeignKey(Product)
	cantidad 			= models.IntegerField()
	fecha_cracion 		= models.DateTimeField(auto_now_add=True)
	fecha_de_entrada 	= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	@models.permalink
	def get_absolute_url(self):
		return ('devolucion_buena', (), { 'devolucion_id': self.id })

	class Meta(object):
		ordering = ['producto',]
		verbose_name = ('Devolucion Buena')
		verbose_name_plural = ('Devoluciones Buenas')


class DevolucionMala(models.Model):
	producto 			= models.ForeignKey(Product)
	cantidad 			= models.IntegerField()
	fecha_cracion 		= models.DateTimeField(auto_now_add=True)
	fecha_de_salida		= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	@models.permalink
	def get_absolute_url(self):
		return ('devolucion_mala', (), { 'devolucion_id': self.id })


	class Meta(object):
		ordering = ['producto',]
		verbose_name = ('Devolucion Mala')
		verbose_name_plural = ('Devoluciones Malas')

class DevolucionReproceso(models.Model):
	producto 			= models.ForeignKey(Product)
	cantidad 			= models.IntegerField()
	fecha_entrada 		= models.DateTimeField(auto_now_add=True)
	fecha_de_entrada	= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	@models.permalink
	def get_absolute_url(self):
		return ('devolucion_reproceso', (), { 'devolucion_id': self.id })

class DevolucionMalaAlmacen(models.Model):
	producto 			= models.ForeignKey(Product)
	cantidad 			= models.IntegerField()
	fecha_cracion 		= models.DateTimeField(auto_now_add=True)
	fecha_de_salida		= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	@models.permalink
	def get_absolute_url(self):
		return ('devolucion_mala_almacen', (), { 'devolucion_almacen_id': self.id })

	class Meta(object):
		ordering = ['producto',]

class DevolucionReprocesoAlmacen(models.Model):
	producto 			= models.ForeignKey(Product)
	cantidad 			= models.IntegerField()
	fecha_entrada 		= models.DateTimeField(auto_now_add=True)
	fecha_de_entrada	= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	@models.permalink
	def get_absolute_url(self):
		return ('devolucion_reproceso_almacen', (), { 'devolucion_almacen_id': self.id })

	class Meta(object):
		ordering = ['producto',]