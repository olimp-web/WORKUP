from django.db import models
from django.contrib.auth.models import User, UserManager


class SkillCategory(models.Model):
    """Категории навыков"""

    name = models.CharField(max_length=30,
                            unique=True,
                            )


class Skill(models.Model):
    """Навыки"""
    name = models.CharField(max_length=128,
                            unique=True,
                            )
    category = models.ForeignKey(SkillCategory)


class Person(models.Model):
    """
        Информация о пользователях
    """

    # Пользовательский уровень приватности
    _PRIVATE_SUFFIX = "_MOD_private"

    user = models.OneToOneField(User)
    user_name = models.CharField(max_length=100,)
    user_surname = models.CharField(max_length=100,)
    gender = models.CharField(max_length=1,
                              choices=(
        ('m', 'Мужской'),
        ('w', 'Женский')
    ))
    birthday = models.DateField()
    birthday_MOD_private = models.TextField(db_column='birthday_MOD_private',
                                            choices=(
        ('1', 'Видно всем'),
        ('2', 'Видно друзьям'),
        ('3', 'Видно колегам')
    ))

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
