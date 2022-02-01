from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('logout/', views.logout_view, name='logout'),
    path('country/', views.country, name='country'),
    path('showplaces/', views.show_places, name='showplaces'),
    path('places/<int:c_id>', views.destination_list, name='destination_list'),
    path('details/<str:name>', views.place_details, name='details'),
    path('booking/<int:place_id>', views.booking, name='booking'),
    path('profile/', views.profile, name='profile'),
    path('summary/', views.booking_summary, name='booking_summary'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='dashboard/password_change.html')),
    path('password_change_done',
         auth_views.PasswordResetDoneView.as_view(template_name='dashboard/password_change_done.html'),
         name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)