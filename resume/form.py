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
                    },
        "contact_email": {"required":"Your Email must not be empty"
                    },
        "subject": {"required":"Your Email must not be empty"
                    },
        "contact_message": {"required":"The message must not be empty"
                    }     
    }
    