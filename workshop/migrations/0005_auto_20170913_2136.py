# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-13 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_auto_20170913_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopregistration',
            name='workshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshop.Workshop'),
        ),
    ]