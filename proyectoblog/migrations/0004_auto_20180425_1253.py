# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-25 15:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoblog', '0003_auto_20180425_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
