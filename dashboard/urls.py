from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page),
    path('logout/', views.logout_view),
    path('country/', views.country),
    path('places/<int:c_id>', views.destination_list, name='destination_list'),
]