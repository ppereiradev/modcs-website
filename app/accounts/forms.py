from django import forms
from django.contrib.auth.forms import UserCreationForm

from.models import User

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()