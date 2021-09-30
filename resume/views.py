from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Profession, Skillarea , Skill,Aboutme, Education, Experience,Service,Portfolio
from .form import ContactForm
from django.http import HttpResponse
from django.core.mail import  BadHeaderError,send_mail
from django.shortcuts import render, redirect
from datetime import date
  
    
class HomePageView(TemplateView):
     template_name = "resume/index.html"

     def get_context_data(self, **kwargs) :
         context = super().get_context_data(**kwargs)
         context ['aboutme'] = Aboutme.objects.all()
         context ['skills'] = Skill.objects.all()
         context ['skillfields'] = Skillarea.objects.all()
         context ['expertises'] = Profession.objects.all()
         context ['educations'] = Education.objects.all()
         context ['experiences'] = Experience.objects.all()
         context ['services'] = Service.objects.all()
         context ['portfolios'] = Portfolio.objects.all()
         context ['form'] = ContactForm()
         context['date'] = date.today
         return context
     
     def post(self,request,*args, **kwargs):
         form = ContactForm(request.POST)
         if form.is_valid():
             subject = form.cleaned_data['subject']
             contact_email = form.cleaned_data['contact_email']
             body = {
                 'contact_name': form.cleaned_data['contact_name'],
                 'contact_email': form.cleaned_data['contact_email'],
                 'contact_message': form.cleaned_data['contact_message']
                 
             }
             email_message ="\n".join(body.values())
             
             print(email_message)
             
             try:
                 send_mail(subject,email_message,f'{contact_email}',['mulendaraphael@yahoo.fr'])
             except BadHeaderError:
                 return HttpResponse('Invalide header found.')
             return redirect("thank-you")
             
         return  HttpResponse('Hello, World!')

    
class ThankYouView(TemplateView):
    template_name = "resume/thank_you.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context ['aboutme'] = Aboutme.objects.all()
        context["message"] = "This works well!"
        context['date'] = date.today
        return context