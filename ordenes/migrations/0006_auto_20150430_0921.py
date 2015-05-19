# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0005_auto_20150424_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenproducto',
            name='linea_total',
        ),
        migrations.RemoveField(
            model_name='ordenproducto',
            name='linea_totalpeso',
        ),
    ]
