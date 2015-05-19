# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('produccion', '0019_auto_20150424_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduccionEsperadaCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_cracion', models.DateTimeField(auto_now_add=True)),
                ('fecha_a_agendar', models.DateField(null=True, blank=True)),
                ('categoria', models.ForeignKey(to='categoria.Categoria')),
            ],
            options={
                'ordering': ['-fecha_a_agendar', '-categoria'],
                'verbose_name': 'Produccion Esperada Categoria',
                'verbose_name_plural': 'Producciones Esperadas Categorias',
            },
            bases=(models.Model,),
        ),
    ]
