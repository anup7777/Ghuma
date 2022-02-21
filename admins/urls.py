from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name="admin_home"),
    path('addcountry/', views.add_country, name='add_country'),
    path('deletecountry/<int:country_id>', views.delete_country),
    path('addplace/', views.add_place),
    path('showplace/', views.show_place),
    path('showusers/', views.get_users),
    path('showadmins/', views.get_admins, name="showadmins"),
    path('deactivate_user/<int:user_id>', views.deactivate_user),
    path('reactive_user/<int:user_id>', views.reactive_user),
    path('bookingdata/', views.booking_date),
    path('updateplace/<int:place_id>', views.update_place),
    path('updatecountry/<int:country_id>', views.update_country),
    path('update_status/<int:pk>', views.update_status, name='update_status'),
    path('contact/', views.contact_form),
    path('logout/', views.logout_view),
]
