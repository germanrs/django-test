# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('laptop', models.ForeignKey(blank=True, to='laptop.Laptop', null=True)),
            ],
        ),
    ]
