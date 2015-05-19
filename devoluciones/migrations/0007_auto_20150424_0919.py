# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devoluciones', '0006_auto_20150305_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devolucionbuena',
            options={'ordering': ['producto'], 'verbose_name': 'Devolucion Buena', 'verbose_name_plural': 'Devoluciones Buenas'},
        ),
        migrations.AlterModelOptions(
            name='devolucionmala',
            options={'ordering': ['producto'], 'verbose_name': 'Devolucion Mala', 'verbose_name_plural': 'Devoluciones Malas'},
        ),
        migrations.AlterModelOptions(
            name='devolucionmalaalmacen',
            options={'ordering': ['producto']},
        ),
        migrations.AlterModelOptions(
            name='devolucionreprocesoalmacen',
            options={'ordering': ['producto']},
        ),
    ]
