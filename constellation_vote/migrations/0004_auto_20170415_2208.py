# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-15 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constellation_vote', '0003_auto_20170413_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='cast_once',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='mechanism',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='poll',
            name='required_winners',
            field=models.IntegerField(default=1),
        ),
    ]
