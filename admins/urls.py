from django.urls import path
from admins import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('logout', views.logout_view, name='logout'),
]