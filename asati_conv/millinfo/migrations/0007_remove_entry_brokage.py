# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('millinfo', '0006_auto_20171015_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='brokage',
        ),
    ]
