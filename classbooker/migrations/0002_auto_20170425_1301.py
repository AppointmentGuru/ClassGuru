# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbooker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]