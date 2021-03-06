# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('millinfo', '0004_auto_20171015_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='total_weight',
        ),
        migrations.AlterField(
            model_name='entry',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='millinfo.Item'),
        ),
    ]
