# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenproducto',
            name='cantidad',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='linea_subtotal',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='linea_subtotalpeso',
            field=models.DecimalField(null=True, max_digits=30, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='linea_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='linea_totalpeso',
            field=models.DecimalField(null=True, max_digits=30, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='unit_price',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
