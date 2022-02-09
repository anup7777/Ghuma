from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('addcountry/', views.add_country),
    path('deletecountry/<int:country_id>', views.delete_country),
    path('addplace/', views.add_place),
    path('showplace/', views.show_place),
    path('showusers/', views.get_users),
    path('showadmins/', views.get_admins),
    path('deactivate_user/<int:user_id>', views.deactivate_user),
    path('reactive_user/<int:user_id>', views.reactive_user),
    path('bookingdata/', views.booking_date),
    path('logout/', views.logout_view),
]