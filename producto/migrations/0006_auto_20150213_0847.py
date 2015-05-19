# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20150205_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['orden'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
