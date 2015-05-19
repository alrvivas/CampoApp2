from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Estado(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta(object):
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados')

class Ciudad(models.Model):
    nombre = models.CharField(max_length=140)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta(object):
        verbose_name = ('Ciudad')
        verbose_name_plural = ('Ciudadades')

class Direccion(models.Model):
    calle = models.CharField(max_length=140)
    colonia = models.CharField(max_length=140,null=True, blank=True)
    cp = models.PositiveIntegerField()
    municipio = models.CharField(max_length=140,null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return u'%s' % self.id

    class Meta(object):
        verbose_name = ('Direccion')
        verbose_name_plural = ('Direcciones')