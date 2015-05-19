# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0002_auto_20150307_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='orden_subtotal',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orden',
            name='orden_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orden',
            name='orden_totalpeso',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
