from django.db import models
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
                                            verbose_name='приватность',
                                            choices=_PRIVATE_CHOICES
                                            )
    city = models.ForeignKey('City',
                             verbose_name='Город')

    skills = models.ManyToManyField(Skill, through='UserSkills')

    class Meta:
        verbose_name = 'личность'
        verbose_name_plural = 'личности'

    def __str__(self):
        return ' '.join([self.user_name, self.user_surname])


class City(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Название")

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name


class Contact(models.Model):
    TYPE = (
        ('e', 'email'),
        ('t', 'Телефон'),
        ('s', 'Ссылка на аккаунт в соц. сети'),
    )

    person = models.ForeignKey(Person)
    type = models.CharField(max_length=1,
                            verbose_name='Способ связи',
                            choices=TYPE)
    content = models.CharField(max_length=100)
    private = models.CharField(max_length=1,
                               choices=_PRIVATE_CHOICES,
                               default='0',
                               verbose_name='Приватность')

    class Meta:
        verbose_name = 'контактная информация'
        verbose_name_plural = 'контактная информация'

    def __str__(self):
        return ': '.join([self.type, self.content])


class UserSkills(models.Model):
    """
        Промежуточная таблица для связи USER <-> SKILL
    """
    person = models.ForeignKey(Person)
    skill = models.ForeignKey(Skill)
    grade = models.SmallIntegerField(help_text='Уровнь владения навыком')
    private = models.CharField(max_length=1,
                               choices=_PRIVATE_CHOICES,
                               default='0',
                               verbose_name='приватность')


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

    class Meta:
        verbose_name = 'высшее образование'
        verbose_name_plural = 'высшие образования'

    def __str__(self):
        return '{}: {} (by {})'.format(self.university, self.group, self.person)
