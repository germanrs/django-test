# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=11)),
                ('uuid', models.CharField(max_length=32)),
                ('modelo', models.CharField(max_length=1, choices=[('1', 'XO-1'), ('2', 'XO-1.5'), ('3', 'XO-1.75'), ('4', 'XO-4')])),
            ],
        ),
    ]
