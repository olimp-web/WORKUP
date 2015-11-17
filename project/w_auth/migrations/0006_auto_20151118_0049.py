# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('w_auth', '0005_auto_20151118_0006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'аккаунт', 'verbose_name_plural': 'аккаунты'},
        ),
        migrations.AddField(
            model_name='account',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
    ]
