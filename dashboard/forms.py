from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user','username','email']



