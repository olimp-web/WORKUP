from django.contrib import admin
from .models import Person, Skill, UserSkills, SkillCategory, Contact, City, Education
# Register your models here.

admin.site.register(Person)
admin.site.register(Skill)
admin.site.register(SkillCategory)
admin.site.register(Contact)
admin.site.register(City)
admin.site.register(Education)

