# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_posts_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='condition',
            field=models.CharField(choices=[('Brand new', 'New'), ('Second hand', 'Used'), ('Damaged', 'Damaged')], default='new', max_length=11),
        ),
        migrations.AlterField(
            model_name='posts',
            name='type',
            field=models.CharField(choices=[('Academic', 'Academics'), ('Office', 'Office')], default='acads', max_length=8),
        ),
    ]
