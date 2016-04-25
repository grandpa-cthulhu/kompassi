# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_auto_20160216_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationinformation',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='S\xe4hk\xf6postiosoite'),
        ),
        migrations.AlterField(
            model_name='shirtorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shirt_order_set', to='tickets.Order'),
        ),
    ]
