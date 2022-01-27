from django.contrib.auth import views as auth_views
from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.index_page, name='home_index'),
    path('login/', views.login, name='login'),
    path('register/', views.register),
    path('home/', views.home, name='home'),
    path('pricing/',views.pricing_page, name='price'),
    path('contact/', views.contact, name='contact'),
    path('country/', views.country_list, name='country'),

    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
    name='password_reset'),
    path('password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),


]