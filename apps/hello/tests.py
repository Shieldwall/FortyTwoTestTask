import datetime

from django.test import TestCase
from .models import User
# Create your tests here.


class HelloTest(TestCase):
    fixtures = ['initial_data']

    def test_fixture_with_personal_data(self):

        '''test makes sure that the fixture with my personal info
        has all info right'''
        s = User.objects.get(pk=1)
        self.assertEquals(s.name, "Alexey")
        self.assertEquals(s.surname, "Shevtsov")
        self.assertEquals(s.date_of_birth, datetime.date(1989, 1, 2))
        self.assertEquals(s.bio, "living")
        self.assertEquals(s.contacts, "muslyaster@gmail.com")
