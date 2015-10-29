from django.db import models
from django.contrib.auth.models import User

from .skill import Skill


class Person(models.Model):
    """
        Информация о пользователях
    """

    # Пользовательский уровень приватности
    _PRIVATE_SUFFIX = "_MOD_private"

    _PRIVATE_CHOICES = (
        ('0', 'Видно только мне'),
        ('1', 'Видно всем'),
        ('2', 'Видно друзьям'),
        ('3', 'Видно колегам'),
    )

    user = models.OneToOneField(User)
    user_name = models.CharField(max_length=100,)
    user_surname = models.CharField(max_length=100,)
    gender = models.CharField(max_length=1,
                              choices=(('m', 'Мужской'),
                                       ('w', 'Женский'))
                              )
    birthday = models.DateField()
    birthday_MOD_private = models.CharField(max_length=1,
                                            db_column='birthday_MOD_private',
                                            choices=_PRIVATE_CHOICES
                                            )

    # def get_pivate(self, attr):
    #     suffix = self._PRIVATE_SUFFIX
    #     # if hasattr(self, (attr.__name__+ suffix)):
    #     return getattr(self, attr.__name__)

#
#
    skills = models.ManyToManyField(Skill, through='UserSkills')


class UserSkills(models.Model):
    person = models.ForeignKey(Person)
    skill = models.ForeignKey(Skill)
    grade = models.SmallIntegerField(help_text='Уровнь владения навыком')
    private = models.CharField(max_length=1,
                               choices=Person._PRIVATE_CHOICES,
                               default='0')
