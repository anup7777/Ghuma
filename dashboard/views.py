from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .filters import PlaceFilter



def index_page(request):
    context = {
        'activate_home': 'active border-bottom active-class'
    }
    return render(request, 'dashboard/index_hm.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def country(request):
    # data = Country.objects.all().order_by('-id')
    context = {
        # 'data': data,
        'activate_explore': 'active border-bottom active-class',
    }
    return render(request, 'dashboard/country_hm.html', context)


def destination_list(request, c_id):
    # dests = Country.objects.get(id=c_id)
    # print(dests)
    context = {
        # 'country': dests
    }
    return render(request, 'dashboard/places.html', context)

def show_places(request):
    # place = Place.objects.all().order_by('-id')
    # place_filter = PlaceFilter(request.GET,queryset=place)
    # place_final = place_filter.qs
    context = {
        # 'places': place_final,
        # 'place_filter': place_filter,
        # 'activate_place': 'active border-bottom active-class h1text'
    }
    return render(request, 'dashboard/showplaces.html', context)


def place_details(request, name):
    # place = Place.objects.get(dest_name=name)
    context = {
        # 'details': place,
        # 'activate_place': 'active'
    }
    return render(request, 'dashboard/details.html', context)

def booking(request, place_id):
    # user = request.user
    # place = Place.objects.get(id=place_id)
    # place_info = Place.objects.filter(id=place_id)
    # offers = Offer.objects.all()

    # if request.method == 'POST':
    #     total_person = request.POST.get('bookin_totalperson')
    #     booked_date = request.POST.get('bookin_date')
    #     place_price = place.dest_price
    #     offer = request.POST.get('bookin_offers')
    #     total_price = int(total_person) * int(place_price)
    #     print(total_price)
    #     bookings = Booking.objects.create(place=place, user=user, offer_id=offer,
    #                                       total_person=total_person, total_price=total_price,
    #                                       booked_date=booked_date, status="In-Review")
    #     if bookings:
            # return redirect('/dashboard/summary')
    context = {
        # 'offers': offers,
        # 'infos': place_info
    }
    return render(request, 'dashboard/booking.html', context)