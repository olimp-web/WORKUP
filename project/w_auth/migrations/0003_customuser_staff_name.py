# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_auth', '0002_auto_20151113_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='staff_name',
            field=models.CharField(max_length=20, default='', blank=True),
        ),
    ]
