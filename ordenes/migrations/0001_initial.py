# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_user'),
        ('empleado', '0002_remove_empleado_direccion'),
        ('producto', '0006_auto_20150213_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('orden_subtotal', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('orden_total', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('orden_totalpeso', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
                ('empleado', models.ForeignKey(blank=True, to='empleado.Empleado', null=True)),
                ('status', models.ForeignKey(blank=True, to='ordenes.Estatus', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrdenProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_price', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('linea_subtotal', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('linea_total', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('linea_subtotalpeso', models.DecimalField(null=True, max_digits=30, decimal_places=3)),
                ('linea_totalpeso', models.DecimalField(null=True, max_digits=30, decimal_places=3)),
                ('orden', models.ForeignKey(blank=True, to='ordenes.Orden', null=True)),
                ('producto', models.ForeignKey(to='producto.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
