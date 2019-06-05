from django.test import TestCase
from .models import UserProfile
from .riot import find_my_rank
from django.db import models

"""
class UserTestCase(TestCase):

    def test_rank(self):
        UserProfile.user = models.CharField(max_length=100, default='')
        user_test = UserProfile.objects.create(user="test", game_tag="lumachino", region="euw1")

        self.assertTrue(user_test.find_my_rank())
"""


class ViewsTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('http://127.0.0.1:8000/profiles/login')
        self.assertEqual(resp.status_code, 200)
