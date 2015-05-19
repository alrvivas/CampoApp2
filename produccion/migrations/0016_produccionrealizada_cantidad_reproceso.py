# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0015_auto_20150205_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccionrealizada',
            name='cantidad_reproceso',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
