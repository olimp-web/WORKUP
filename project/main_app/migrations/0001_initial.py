# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(help_text='Название', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=16)),
                ('content', models.CharField(max_length=100)),
                ('private', models.CharField(choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], max_length=1, default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('university', models.CharField(verbose_name='Университет', max_length=100)),
                ('subdivision', models.CharField(help_text='Подразделение, факультет', max_length=100, verbose_name='Подразделение')),
                ('department', models.CharField(help_text='кафедра', max_length=100, verbose_name='Кафедра')),
                ('begin_year', models.SmallIntegerField(help_text='Начало обучения', verbose_name='Год начала обучения')),
                ('end_year', models.SmallIntegerField(help_text='Окончание обучения', verbose_name='Год окончания обучения')),
                ('group', models.CharField(help_text='Группа', max_length=10, verbose_name='Группа')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user_name', models.CharField(verbose_name='Имя', max_length=100)),
                ('user_surname', models.CharField(verbose_name='Фамилия', max_length=100)),
                ('gender', models.CharField(verbose_name='Пол', max_length=1, choices=[('m', 'Мужской'), ('w', 'Женский')])),
                ('birthday', models.DateField()),
                ('birthday_MOD_private', models.CharField(choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], max_length=1, db_column='birthday_MOD_private')),
                ('city', models.ForeignKey(verbose_name='Город', to='main_app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('grade', models.SmallIntegerField(help_text='Уровнь владения навыком')),
                ('private', models.CharField(choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], max_length=1, default='0')),
                ('person', models.ForeignKey(to='main_app.Person')),
                ('skill', models.ForeignKey(to='main_app.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(to='main_app.SkillCategory'),
        ),
        migrations.AddField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(to='main_app.Skill', through='main_app.UserSkills'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='education',
            name='person',
            field=models.ForeignKey(to='main_app.Person'),
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(to='main_app.Person'),
        ),
    ]
