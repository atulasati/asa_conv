# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('millinfo', '0007_remove_entry_brokage'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='mill_brokage',
            field=models.FloatField(default=2),
        ),
        migrations.AddField(
            model_name='entry',
            name='party_brokage',
            field=models.FloatField(default=3),
        ),
        migrations.AlterField(
            model_name='entry',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='millinfo.Item'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='weight_per_bag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='millinfo.Weight'),
        ),
    ]
