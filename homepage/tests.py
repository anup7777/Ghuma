from urllib import response
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User



# the testing of the crude operation used #

class Testviews(TestCase):
    # from customer views test 
    def test_customer_view(self):
        user=User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client= Client()
        logged_in=client.login(username="testcase",password="123")
        url = reverse('admin_home')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"admins/admins_home.html")

    # from booking views test 

    def test_booking_view(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('booking_summary')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'dashboard/summary.html')


    # views from the country  ## 

    def test_country_view(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase", password="123")
        url=reverse('country')
        response = client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"dashboard/country_hm.html")

    def test_country_add(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('add_country')
        response = client.post(url,{
            'name':"testgamename",
            'description' : "describe",
            'number':"testnumber",
            'bgurl' : "testbgurl",
            'image' : 'testimage',
     
        })
        self.assertEquals(response.status_code,200)
        self.assertRedirects(response,'admins/add_country.html',)

    #   view from the user app 
    def test_user_view(self):
        user = User.objects.create(username="testcase")
        user.set_password('123')
        user.save()
        client = Client()
        logged_in = client.login(username="testcase",password="123")
        url = reverse('showadmins')
        response = client.get(url)
        self.assertEquals(response.status_code,302)
        self.assertTemplateUsed(response,'admins/show_admins.html')

