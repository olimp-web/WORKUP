# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20151028_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(null=True, max_length=254, default=None, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email_MOD_private',
            field=models.CharField(max_length=1, default='0', choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')]),
        ),
        migrations.AddField(
            model_name='userskills',
            name='private',
            field=models.CharField(max_length=1, default='0', choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday_MOD_private',
            field=models.CharField(db_column='birthday_MOD_private', max_length=1, choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')]),
        ),
    ]
