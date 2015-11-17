from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from .skill import Skill

_PRIVATE_CHOICES = (
    ('0', 'Видно только мне'),
    ('1', 'Видно всем'),
    ('2', 'Видно друзьям'),
    ('3', 'Видно колегам'),
)


class Person(models.Model):
    """
        Информация о пользователях
    """

    # Пользовательский уровень приватности

    _PRIVATE_SUFFIX = "_MOD_private"

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    user_name = models.CharField(max_length=100,
                                 verbose_name='Имя')
    user_surname = models.CharField(max_length=100,
                                    verbose_name='Фамилия')

    gender = models.CharField(max_length=1,
                              verbose_name='Пол',
                              choices=(('m', 'Мужской'),
                                       ('w', 'Женский'))
                              )
    birthday = models.DateField()
    birthday_MOD_private = models.CharField(max_length=1,
                                            db_column='birthday_MOD_private',
                                            choices=_PRIVATE_CHOICES
                                            )
    city = models.ForeignKey('City',
                             verbose_name='Город')

    skills = models.ManyToManyField(Skill, through='UserSkills')
    def __str__(self):
        return '%s' %(self.user_name)

class City(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Название")
    def __str__(self):
        return self.name



class Contact(models.Model):
    person = models.ForeignKey(Person)
    type = models.CharField(max_length=16)
    content = models.CharField(max_length=100)
    private = models.CharField(max_length=1,
                               choices=_PRIVATE_CHOICES,
                               default='0')


class UserSkills(models.Model):
    """
        Промежуточная таблица для связи USER <-> SKILL
    """
    person = models.ForeignKey(Person)
    skill = models.ForeignKey(Skill)
    grade = models.SmallIntegerField(help_text='Уровнь владения навыком')
    private = models.CharField(max_length=1,
                               choices=_PRIVATE_CHOICES,
                               default='0')


class Education(models.Model):
    person = models.ForeignKey(Person)

    university = models.CharField(max_length=100,
                                  verbose_name="Университет")
    subdivision = models.CharField(max_length=100,
                                   verbose_name="Подразделение",
                                   help_text="Подразделение, факультет")
    department = models.CharField(max_length=100,
                                  verbose_name="Кафедра",
                                  help_text="кафедра")
    begin_year = models.SmallIntegerField(verbose_name="Год начала обучения",
                                          help_text="Начало обучения")
    end_year = models.SmallIntegerField(verbose_name="Год окончания обучения",
                                        help_text="Окончание обучения",)
    group = models.CharField(max_length=10,
                             verbose_name="Группа",
                             help_text="Группа")
    def __str__(self):
        return ", ".join([self.university, self.subdivision, self.department])
