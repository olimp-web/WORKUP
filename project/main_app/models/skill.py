from django.db import models


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
