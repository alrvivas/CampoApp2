# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0004_auto_20150424_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenproducto',
            name='producto',
            field=models.ForeignKey(default=1, to='producto.Product'),
            preserve_default=False,
        ),
    ]
