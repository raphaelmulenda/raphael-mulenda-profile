from django.contrib import admin
from django.db import models
from .models import Profession, Aboutme, Skillarea , Skill
# Register your models here.

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id','work_profession')
    list_display_links =('id','work_profession')

admin.site.register(Profession,ProfessionAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display =('id','first_name','last_name','about_me')
    list_display_links= ('id','first_name')
    
admin.site.register(Aboutme, AboutAdmin)


class SkillareaAdmin(admin.ModelAdmin):
    list_display=('id','area_skill')
    list_display_links=('id','area_skill')
    
admin.site.register(Skillarea,SkillareaAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display=('id','skill_branch','skill_level','area_of_work')
    list_display_links=('id','skill_branch')
    search_fields=('area_of_work','skill_branch','skill_level')
    
admin.site.register(Skill,SkillAdmin)