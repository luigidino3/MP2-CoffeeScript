# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20170815_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='marketplace.Posts'),
        ),
    ]
