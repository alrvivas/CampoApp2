# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20150424_0919'),
        ('ordenes', '0007_auto_20150430_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDevolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_price', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('linea_subtotal', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('linea_subtotalpeso', models.DecimalField(null=True, max_digits=30, decimal_places=3, blank=True)),
                ('orden', models.ForeignKey(blank=True, to='ordenes.Orden', null=True)),
                ('producto', models.ForeignKey(to='producto.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
