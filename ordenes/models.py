from django.db import models
from django.contrib.auth.models import User
from empleado.models import Empleado
from cliente.models import Cliente
from producto.models import Product


class TipoPago(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return unicode(self.nombre)


class Estatus(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return unicode(self.nombre)


class Orden(models.Model):
    empleado = models.ForeignKey(Empleado, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    status = models.ForeignKey(Estatus, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    orden_subtotal = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    orden_total = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    orden_totalpeso = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return('orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_urlo(self):
        return('orden-pendiente', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_urle(self):
        return('orden-exitosa', (), { 'orden_id': self.id })

    def __unicode__(self):
        return unicode(self.id)

    class Meta(object):
        verbose_name = ('Orden')
        verbose_name_plural = ('Ordenes')


class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, null=True, blank=True)
    producto = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    linea_subtotal = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    linea_subtotalpeso = models.DecimalField(max_digits=30, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s"% (self.orden, self.producto)


class OrdenDevolucion(models.Model):
    orden = models.ForeignKey(Orden, null=True, blank=True)
    producto = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    linea_subtotal = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    linea_subtotalpeso = models.DecimalField(max_digits=30, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return "%s - %s"% (self.orden, self.producto)
	
