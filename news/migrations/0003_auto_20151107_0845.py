# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_ready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_body',
            field=models.CharField(default=b'', max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date_published'),
        ),
    ]
