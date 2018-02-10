# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-10 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='success_rate',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='total_capacity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]