#encoding:utf-8
from django.db import models

from producto.models import Product
from categoria.models import Categoria

class ProduccionEsperadaCategoria(models.Model):
	categoria 		= models.ForeignKey(Categoria)
	cantidad 		= models.IntegerField()
	fecha_cracion 	= models.DateTimeField(auto_now_add=True)
	fecha_a_agendar = models.DateField(null=True,blank=True)

	def __unicode__(self):
	    return "%s - %s"% (self.producto, self.fecha_a_agendar)

	class Meta(object):
		ordering = ['-fecha_a_agendar','-categoria']
		verbose_name = ('Produccion Esperada Categoria')
		verbose_name_plural = ('Producciones Esperadas Categorias')

	

class ProduccionEsperada(models.Model):
	producto 		= models.ForeignKey(Product)
	cantidad 		= models.IntegerField()
	fecha_cracion 	= models.DateTimeField(auto_now_add=True)
	fecha_a_agendar = models.DateField(null=True,blank=True)
	realizada		= models.BooleanField(default=True)

	def __unicode__(self):
	    return "%s - %s"% (self.producto, self.fecha_a_agendar)

	class Meta(object):
		ordering = ['-fecha_a_agendar','-producto']
		verbose_name = ('Produccion Esperada')
		verbose_name_plural = ('Producciones Esperadas')

	@models.permalink
	def get_absolute_url(self):
		return ('esperada', (), { 'produccione_id': self.id })





class ProduccionRealizada(models.Model):
	producto 				= models.ForeignKey(Product)
	produccion_esperada		= models.ForeignKey(ProduccionEsperada)
	cantidad 				= models.IntegerField()
	cantidad_reproceso 		= models.IntegerField(null=True,blank=True,default=0)
	fecha_cracion 			= models.DateTimeField(auto_now_add=True)
	fecha_de_elaboracion 	= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	def __unicode__(self):
	    return unicode(self.producto)

	class Meta(object):
		ordering = ['producto']
		verbose_name = ('Produccion Realizada')
		verbose_name_plural = ('Producciones Realizada')

	@models.permalink
	def get_absolute_url(self):
		return ('realizada', (), { 'produccionr_id': self.id })

	def produccion_kilos(self):
	    return self.producto.peso*self.cantidad

	def produccion_kilos(self):
	    return self.producto.peso*self.cantidad_reproceso

	def produccion_total(self):
	    return self.cantidad+self.cantidad_reproceso

	def get_rendimiento(self):
		if self.cantidad == 0 or self.produccion_esperada.cantidad == 0:
			return 0
		else:
			return (float(self.cantidad)/float(self.produccion_esperada.cantidad))*100
		

	    

	
