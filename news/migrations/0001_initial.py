# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_title', models.CharField(max_length=100)),
                ('news_body', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date_published')),
            ],
        ),
    ]
