from django.urls import path
from . import views

from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path("home", views.HomePageView.as_view(), name='home'),
    #path('about',views.WorkProfessionView.as_view())
    path('thank-you', views.ThankYouView.as_view(), name='thank-you'),
    #path('pdf/', views.GeneratePdf.as_view()),
    #path('home-page', views.pdf_generation) ,
    #path('', PDFTemplateView.as_view(template_name='my_template.html', filename='my_pdf.pdf', name='pdf')),
    ]
    
