# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]