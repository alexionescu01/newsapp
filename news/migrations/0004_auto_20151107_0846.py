# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20151107_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_body',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date_published'),
        ),
    ]
