# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_auto_20150213_0847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['categoria', 'orden'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
