import django_filters
from dashboard.models import Booking


class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = ['place']