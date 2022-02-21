from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from dashboard.views import booking_summary, index_page, country, show_places, profile
from django.contrib.auth.models import User
from urllib import response



# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse("index_page")
        print(resolve(url))
        self.assertEquals(resolve(url).func,index_page)

    def test_case_summary_url(self):
        url=reverse("booking_summary")
        print(resolve(url))
        self.assertEquals(resolve(url).func,booking_summary)

    def test_case_country_url(self):
        url=reverse("country")
        print(resolve(url))
        self.assertEquals(resolve(url).func, country)

    def test_case_show_places_url(self):
        url=reverse("showplaces")
        print(resolve(url))
        self.assertEquals(resolve(url).func, show_places)

    def test_case_user_profile_url(self):
        url=reverse("profile")
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)



