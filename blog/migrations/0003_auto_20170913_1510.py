# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170913_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
