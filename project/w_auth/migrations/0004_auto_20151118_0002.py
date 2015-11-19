# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('w_auth', '0003_customuser_staff_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=254, verbose_name='email address', unique=True)),
                ('staff_name', models.CharField(max_length=20, default='', blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set', blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user')),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'account',
            },
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', related_name='C_user_set', blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_name='C_user_set', blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user'),
        ),
    ]
