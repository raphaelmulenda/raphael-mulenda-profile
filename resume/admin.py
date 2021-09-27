from django.contrib import admin
from django.db import models
from .models import Portfolio, Profession, Aboutme, Skillarea , Skill, Education,Experience,Service
# Register your models here.

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id','work_profession')
    list_display_links =('id','work_profession')

admin.site.register(Profession,ProfessionAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display =('id','first_name','last_name','about_me','phon_number','email_address')
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

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','study_level','study_field','university','city','country','start_date','end_date','university_url')
    list_display_links = ('id','study_level')
    list_filter = ('study_level','university')
    
admin.site.register(Education,EducationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id','company','work_position','city','country','start_date','end_date','is_current_job','job_description')
    list_display_links = ('id','company','work_position')
    list_filter = ('company','work_position')
    list_editable = ('is_current_job',)
    
admin.site.register(Experience,ExperienceAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_area', 'service_url', 'service_description')
    list_display_links = ('id', 'service_area')
    list_filter = ('service_area',)
    
admin.site.register(Service,ServiceAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','project_area','project_name','project_description','project_url')
    list_filter = ('project_area','project_name')
    list_display_links = ('id','project_area')
    prepopulated_fields = {"slug":("project_area",)}

admin.site.register(Portfolio,PortfolioAdmin)



