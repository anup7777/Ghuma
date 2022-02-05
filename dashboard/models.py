from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import validators
from django.core.validators import *


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[validate_email])
    phone = models.CharField(max_length=10, null=True, validators=[validators.MinLengthValidator(7)])
    profile_pic = models.FileField(upload_to='static/uploads/profile', default='static/images/user.png')
    created_date = models.DateTimeField(auto_now_add=True)

