# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_auto_20161021_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
