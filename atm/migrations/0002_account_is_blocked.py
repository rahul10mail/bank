# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
