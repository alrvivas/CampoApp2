# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devoluciones', '0005_devolucionmalaalmacen_devolucionreprocesoalmacen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devolucionbuena',
            options={'ordering': ['fecha_de_entrada', '-producto'], 'verbose_name': 'Devolucion Buena', 'verbose_name_plural': 'Devoluciones Buenas'},
        ),
        migrations.AlterModelOptions(
            name='devolucionmala',
            options={'ordering': ['fecha_de_salida', '-producto'], 'verbose_name': 'Devolucion Mala', 'verbose_name_plural': 'Devoluciones Malas'},
        ),
    ]
