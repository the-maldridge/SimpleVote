# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-04 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constellation_vote', '0003_auto_20170404_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polloption',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constellation_vote.Poll'),
        ),
        migrations.AlterField(
            model_name='polloption',
            name='text',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
