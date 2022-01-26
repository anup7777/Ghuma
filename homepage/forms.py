from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from homepage.models import ContactForm


class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields = ('first_name','last_name','username','email','password1','password2')


class ContactForms(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'


