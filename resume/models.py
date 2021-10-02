from datetime import date
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator , MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Profession(models.Model):
    work_profession = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.work_profession}"
    
    
class Skillarea(models.Model):
    area_skill = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return f"{self.area_skill}"

class Skill(models.Model):
    skill_branch = models.CharField(max_length=100, blank=True)
    skill_level =models.IntegerField(default =1, validators=[MaxValueValidator(100),MinValueValidator(1)],blank=True, null=True)
    area_of_work = models.ForeignKey(Skillarea,  on_delete=models.CASCADE,blank=True)
    
    def __str__(self):
        return f"{self.area_of_work}" f"{self.skill_branch}" f"{self.skill_level}"
    
    
    
class Aboutme(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about_me = models.TextField(validators=[MinLengthValidator(10)])
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_sidbar = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_about = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    professions = models.ManyToManyField(Profession,blank=True)
    email_address = models.EmailField(max_length=100,blank=True)
    phon_number = models.CharField(max_length=100)
    city = models.CharField(max_length=50,blank=True)
    country =models.CharField(max_length=50,blank=True)
    social_media_1_name = models.CharField(max_length=50, blank=True)
    social_media_1_url = models.URLField(blank=True)
    social_media_1_icon = models.CharField(max_length=50, blank=True)
    social_media_2_name = models.CharField(max_length=50, blank=True)
    social_media_2_url = models.URLField(blank=True)
    social_media_2_icon = models.CharField(max_length=50, blank=True)
    social_media_3_name = models.CharField(max_length=50, blank=True)
    social_media_3_url = models.URLField(blank=True)
    social_media_3_icon = models.CharField(max_length=50, blank=True)
    social_media_4_name = models.CharField(max_length=50, blank=True)
    social_media_4_url = models.URLField(blank=True)
    social_media_4_icon = models.CharField(max_length=50, blank=True)
    social_media_5_name = models.CharField(max_length=50, blank=True)
    social_media_5_url = models.URLField(blank=True)
    social_media_5_icon = models.CharField(max_length=50, blank=True)
    social_media_6_name = models.CharField(max_length=50, blank=True)
    social_media_6_url = models.URLField(blank=True)
    social_media_6_icon = models.CharField(max_length=50, blank=True)
    upload_cv = models.FileField(upload_to='resume/%Y/%m/%d/', blank =True)
    
    #skill =models.ForeignKey(Skill,on_delete=models.CASCADE,blank=True, default=None)
    
    def __str__(self):
        return f"{self.first_name}" f"{self.last_name}" f"{self.professions}" f"{self.about_me}"
    

class Education(models.Model):
    study_level = models.CharField(max_length=50)
    study_field = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    university_url = models.URLField(blank=True)
    city = models.CharField(max_length=50)
    country =models.CharField(max_length=50)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    
    def __str__(self):
        return f"{self.study_level}" f"{self.study_level}" f"{self.university}" f"{self.university_url}"
    

class Experience(models.Model):
    company = models.CharField(max_length=100)
    work_position = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    is_current_job = models.BooleanField(default=True)
    job_description = models.TextField(validators=[MinLengthValidator(20)])
    
    def __str__(self):
        return f"{self.company}" f"{self.work_position}" 
    

class Service(models.Model):
    service_area = models.CharField(max_length=200)
    service_url = models.CharField(max_length=50)
    service_description = models.TextField(validators=[MinLengthValidator(15)])
    
    def __str__(self):
        return  f"{self.service_area}"
        
class Portfolio(models.Model):
    project_area = models.CharField(max_length=50)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=100)
    project_url = models.URLField(blank=True)
    project_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    slug = models.SlugField(default="",blank=True)
    
    
    def __str__(self):
        return  f"{self.project_area}"  f"{self.project_name}"  f"{self.project_description}"


class Contact(models.Model):
    contact_name = models.CharField(max_length=120,blank=False,error_messages={'required': 'Please enter your name'})
    contact_email = models.EmailField(blank=False,error_messages={'required': 'Please enter your Email'})
    subject = models.CharField(max_length=50,blank=False, error_messages={'required': 'Please enter a subject'})
    contact_message = models.TextField(blank=False,error_messages={'required': 'Please enter your message here'})
    
    def __str__(self):
        return f"{self.contact_name}"   f"{self.contact_email}" f"{self.subject}" 