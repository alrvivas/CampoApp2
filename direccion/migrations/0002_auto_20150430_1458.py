# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('estado', models.ForeignKey(to='direccion.Estado')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudadades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=140)),
                ('colonia', models.CharField(max_length=140, null=True, blank=True)),
                ('cp', models.PositiveIntegerField()),
                ('municipio', models.CharField(max_length=140, null=True, blank=True)),
                ('ciudad', models.ForeignKey(to='direccion.Ciudad')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='address',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user_billing',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user_shipping',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='name',
            new_name='nombre',
        ),
    ]
