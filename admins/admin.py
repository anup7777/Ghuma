from django.contrib import admin
from .models import Country, Place
from dashboard.models import Booking

# Register your models here.

admin.site.register(Country)
admin.site.register(Booking)
admin.site.register(Place)
