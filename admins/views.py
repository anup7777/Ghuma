from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'admins/admins_home.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')