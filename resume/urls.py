from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    #path('about',views.WorkProfessionView.as_view())
    path("contact", views.ContactView.as_view(), name='contact')
    ]