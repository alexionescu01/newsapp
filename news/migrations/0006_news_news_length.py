# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20151107_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_length',
            field=models.IntegerField(default=0),
        ),
    ]
