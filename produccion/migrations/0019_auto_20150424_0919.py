# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0018_auto_20150305_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produccionrealizada',
            options={'ordering': ['producto'], 'verbose_name': 'Produccion Realizada', 'verbose_name_plural': 'Producciones Realizada'},
        ),
    ]
