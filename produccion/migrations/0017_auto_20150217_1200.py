# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0016_produccionrealizada_cantidad_reproceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccionrealizada',
            name='cantidad_reproceso',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
