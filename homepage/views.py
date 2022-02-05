from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout
from . import forms, models
from .forms import SignupForm, ContactForms
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    context = {
        'activate_hhomepage': 'active border-bottom active-class',
    }
    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if not user.is_staff:
                auth.login(request, user)
                return redirect('/dashboard')

            elif user.is_staff:
                auth.login(request, user)
                return redirect('/admins')

        else:
            messages.add_message(request, messages.ERROR, "Invalid Username and Password!")
            return render(request, 'homepage/login.html')

    else:
        return render(request, 'login.html') 

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request, messages.SUCCESS, "User has been created successfully!")
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, "Failed to create an account, Check carefully and Try Again!")
            return render(request, 'homepage/register.html', {'form': form})

    form = SignupForm
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def pricing_page(request):
    context = {
        'active_pricing': 'active',
        'activate_hpricing': 'active border-bottom active-class'
    }
    return render(request, 'pricing.html', context)

def country_list(request):
    # data = Country.objects.all().order_by('-id')
    context = {
        # 'data': data,
        'activate_hcountry': 'active border-bottom active-class'
    }
    return render(request, 'country.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Contact form has been submitted")
            return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, "Error")
            return redirect('/contact')
    context = {
        'form': ContactForms
    }
    return render(request, 'contact.html', context)

