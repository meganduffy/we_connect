# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 15:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0002_auto_20170312_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 14, 15, 0, 23, 704000, tzinfo=utc)),
        ),
    ]
