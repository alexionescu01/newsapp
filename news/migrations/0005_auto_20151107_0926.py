# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20151107_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
    ]
