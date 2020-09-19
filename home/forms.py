from django import forms
from django.forms import ModelForm
from .models import NewUser
from django.contrib.auth.models import User

class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ['first_name', 'last_name', 'email', 'password', 'bio']
        widgets = {
            'password': forms.PasswordInput()
        }


