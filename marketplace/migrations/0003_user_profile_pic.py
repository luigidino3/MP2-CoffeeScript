# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_posts_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
