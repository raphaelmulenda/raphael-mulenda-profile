from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Profession, Skillarea , Skill,Aboutme

# Create your views here.


# class HomePageView(ListView):
#     template_name = "resume/home.html"
#     model = Aboutme
#     context_object_name = "aboutme"
    
    
# class HomePageView(ListView):
#     template_name = "resume/home.html"
#     model = Aboutme
#     context_object_name = "aboutme"
    
    
            
    
    
# class WorkProfessionView(ListView):
#     template_name = "resume/home.html"
#     model = Profession
#     context_object_name = "works"
    
    

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     Skills = Skill.objects.all()
    #     context["skills"] = Skills
    #     return context
    
    
class HomePageView(TemplateView):
     template_name = "resume/index.html"
     
     def get_context_data(self, **kwargs) :
         context = super().get_context_data(**kwargs)
         context ['aboutme'] = Aboutme.objects.all()
         context ['skills'] = Skill.objects.all()
         context ['skillfields'] = Skillarea.objects.all()
         context ['expertises'] = Profession.objects.all()
         return context
    