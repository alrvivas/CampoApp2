# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0003_auto_20150307_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenproducto',
            name='producto',
            field=models.ForeignKey(blank=True, to='producto.Product', null=True),
            preserve_default=True,
        ),
    ]
