# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_auto_20150213_0847'),
        ('devoluciones', '0004_auto_20150205_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevolucionMalaAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_cracion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_salida', models.DateField(null=True, blank=True)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('producto', models.ForeignKey(to='producto.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DevolucionReprocesoAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_entrada', models.DateField(null=True, blank=True)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('producto', models.ForeignKey(to='producto.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
