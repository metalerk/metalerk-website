# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
