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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Название', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=16)),
                ('content', models.CharField(max_length=100)),
                ('private', models.CharField(choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('university', models.CharField(verbose_name='Университет', max_length=100)),
                ('subdivision', models.CharField(help_text='Подразделение, факультет', verbose_name='Подразделение', max_length=100)),
                ('department', models.CharField(help_text='кафедра', verbose_name='Кафедра', max_length=100)),
                ('begin_year', models.SmallIntegerField(help_text='Начало обучения', verbose_name='Год начала обучения')),
                ('end_year', models.SmallIntegerField(help_text='Окончание обучения', verbose_name='Год окончания обучения')),
                ('group', models.CharField(help_text='Группа', verbose_name='Группа', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user_name', models.CharField(verbose_name='Имя', max_length=100)),
                ('user_surname', models.CharField(verbose_name='Фамилия', max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Мужской'), ('w', 'Женский')], verbose_name='Пол', max_length=1)),
                ('birthday', models.DateField()),
                ('birthday_MOD_private', models.CharField(choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], db_column='birthday_MOD_private', max_length=1)),
                ('city', models.ForeignKey(to='main_app.City', verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('grade', models.SmallIntegerField(help_text='Уровнь владения навыком')),
                ('private', models.CharField(choices=[('0', 'Видно только мне'), ('1', 'Видно всем'), ('2', 'Видно друзьям'), ('3', 'Видно колегам')], default='0', max_length=1)),
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
            field=models.ManyToManyField(through='main_app.UserSkills', to='main_app.Skill'),
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
