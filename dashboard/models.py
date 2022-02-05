from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import validators
from django.core.validators import *
from admins.models import Place, Country


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=50, null=True, validators=[validators.MinLengthValidator(2)])
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[validate_email])
    phone = models.CharField(max_length=10, null=True, validators=[validators.MinLengthValidator(7)])
    profile_pic = models.FileField(upload_to='static/uploads/profile', default='static/images/user.png')
    created_date = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    STATUS = (
        ('In-Review', 'In-Review'),
        ('Confirmed', 'Confirmed'),
        ('Denied', 'Denied'),
    )
    place = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    total_person = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    booked_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)