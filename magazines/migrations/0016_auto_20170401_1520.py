# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 14:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0015_auto_20170401_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 1, 14, 20, 29, 925000, tzinfo=utc)),
        ),
    ]
