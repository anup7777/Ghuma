import django_filters
from django_filters import CharFilter


class PlaceFilter(django_filters.FilterSet):
    dest_search = CharFilter(field_name='dest_name',lookup_expr='icontains')