# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_video_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brief',
            field=models.TextField(default='', verbose_name='简介'),
        ),
    ]
