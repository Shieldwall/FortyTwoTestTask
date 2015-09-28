import datetime

from django.test import TestCase
from .models import *
# Create your tests here.


class HelloTest(TestCase):
    fixtures = ['hello']

    def test_fixture_with_personal_data(self):
        s = User.objects.get(pk=1)
        self.assertEquals(s.name, "Alexey")
        self.assertEquals(s.surname, "Shevtsov")
        self.assertEquals(s.date_of_birth, datetime.date('1989', '1', '2'))
        self.assertEquals(s.bio, "living")
        self.assertEquals(s.contacts, "muslyaster@gmail.com")
