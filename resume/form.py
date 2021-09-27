from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {"contact_name":"Your Name",
                 "contact_email":"Your Email",
                 "subject":"Subject",
                 "contact_message":"Message",
                 
    }
    error_messages = {
        "contact_name":{"required":"Your Name must not be empty"
                    }
        
    
    }