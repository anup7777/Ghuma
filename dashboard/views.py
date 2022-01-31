from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout



def index_page(request):
    context = {
        'activate_home': 'active border-bottom active-class'
    }
    return render(request, 'index_hm.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def country(request):
    # data = Country.objects.all().order_by('-id')
    context = {
        # 'data': data,
        'activate_explore': 'active border-bottom active-class',
    }
    return render(request, 'country_hm.html', context)


def destination_list(request, c_id):
    # dests = Country.objects.get(id=c_id)
    # print(dests)
    context = {
        # 'country': dests
    }
    return render(request, 'places.html', context)