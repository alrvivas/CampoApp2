# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salidas', '0005_auto_20150213_0854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salida',
            options={'ordering': ['fecha_de_salida', '-producto'], 'verbose_name': 'Salida', 'verbose_name_plural': 'Salidas'},
        ),
    ]
