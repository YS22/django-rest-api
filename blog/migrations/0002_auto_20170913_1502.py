# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='status',
            field=models.CharField(choices=[('draft', '\u8349\u7a3f'), ('public', '\u516c\u5f00')], default='public', max_length=8),
        ),
    ]
