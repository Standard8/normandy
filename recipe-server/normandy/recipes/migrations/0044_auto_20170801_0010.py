# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-01 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0043_auto_20170727_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='implementation_hash',
            field=models.CharField(editable=False, max_length=71),
        ),
    ]