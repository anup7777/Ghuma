from django.db import models
from django.core import validators
from django.core.validators import *


# Country
class Country(models.Model):
    Name = models.CharField(max_length=120, null=False, validators=[validators.MinLengthValidator(2)],db_index=True)
    Description = models.CharField(max_length=60, validators=[validators.MinLengthValidator(30)])
    Number = models.IntegerField(validators=[validators.integer_validator])
    bg_url = models.URLField(validators=[validators.URLValidator])
    Image = models.ImageField(upload_to="static/uploads/country")

    def __str__(self):
        return self.Name


# Places inside country
class Place(models.Model):
    dest_name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(5)],db_index=True)
    dest_type = models.CharField(max_length=50, validators=[validators.MinLengthValidator(3)])
    dest_price = models.IntegerField(validators=[validators.integer_validator])
    dest_desc = models.TextField(validators=[validators.MaxLengthValidator(1000)])
    dest_location = models.CharField(max_length=120)
    dest_image = models.ImageField(upload_to="static/uploads/destination",validators=[validators.URLValidator])
    day_one = models.TextField(validators=[validators.MaxLengthValidator(1000)])
    total_person = models.IntegerField(default=2)
    day_two = models.TextField(validators=[validators.MaxLengthValidator(1000)])
    day_three = models.TextField(validators=[validators.MaxLengthValidator(1000)])
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.dest_name
