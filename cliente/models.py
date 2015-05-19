from django.db import models
from django.contrib.auth.models import User
from direccion.models import Direccion

class Tipo_Cliente(models.Model):
	nombre		= models.CharField(max_length=140)

	def __unicode__(self): 
		return self.nombre

class Cliente(models.Model):
	user = models.ForeignKey(User, unique=True)
	tipo = models.ForeignKey(Tipo_Cliente)
	nombre = models.CharField(max_length=140,null=True, blank=True)
	rfc	= models.CharField(max_length=140,null=True, blank=True)
	telefono1 = models.CharField(max_length=20,null=True, blank=True)
	telefono2 = models.CharField(max_length=20,null=True, blank=True)
	celullar = models.CharField(max_length=20,null=True, blank=True)
	email = models.CharField(max_length=80,null=True, blank=True)
	direccion = models.ManyToManyField(Direccion,null=True, blank=True)	

	def __unicode__(self): 
		return self.nombre

	@models.permalink
	def get_absolute_url(self):
		return('cleinte', (), { 'cliente_id': self.id })