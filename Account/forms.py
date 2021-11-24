from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from Account.models import *


class RegistrationForm(UserCreationForm):
    fullname = forms.CharField(max_length=150)
    contact = forms.CharField(max_length=10)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("fullname", "contact",
                  "email", "password1", "password2")
