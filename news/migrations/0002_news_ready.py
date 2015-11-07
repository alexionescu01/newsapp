# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ready',
            field=models.BooleanField(default=datetime.datetime(2015, 11, 7, 8, 28, 38, 264181, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
