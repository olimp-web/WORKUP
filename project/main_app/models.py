from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.


class UserProfile(models.Model):
    """Информация о пользователях"""
    user = models.OneToOneField(User)



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
