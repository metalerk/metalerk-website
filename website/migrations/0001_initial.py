# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('contenido', models.TextField(max_length=1000)),
                ('actualizado', models.DateField(auto_now=True)),
                ('registro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
