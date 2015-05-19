# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salidas', '0006_auto_20150305_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salida',
            options={'ordering': ['producto'], 'verbose_name': 'Salida', 'verbose_name_plural': 'Salidas'},
        ),
    ]
