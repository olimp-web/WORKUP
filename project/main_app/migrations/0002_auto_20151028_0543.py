# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_surname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Мужской'), ('w', 'Женский')], max_length=1)),
                ('birthday', models.DateField()),
                ('birthday_MOD_private', models.TextField(choices=[('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], db_column='birthday_MOD_private')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('grade', models.SmallIntegerField(help_text='Уровнь владения навыком')),
                ('person', models.ForeignKey(to='main_app.Person')),
                ('skill', models.ForeignKey(to='main_app.Skill')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(through='main_app.UserSkills', to='main_app.Skill'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
