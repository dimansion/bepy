# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0007_userproject_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
