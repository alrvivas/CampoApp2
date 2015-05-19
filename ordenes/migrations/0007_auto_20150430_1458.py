# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0006_auto_20150430_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orden',
            options={'verbose_name': 'Orden', 'verbose_name_plural': 'Ordenes'},
        ),
    ]
