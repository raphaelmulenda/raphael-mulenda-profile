from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="starting-page"),
    #path('about',views.WorkProfessionView.as_view())
    path('thank-you', views.ThankYouView.as_view(), name='thank-you'),
    
    ]
    
