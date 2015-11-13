# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0012_auto_20151017_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='time_confirmation_requested',
            field=models.DateTimeField(null=True, verbose_name='Vahvistusta vaadittu', blank=True),
            preserve_default=True,
        ),
    ]