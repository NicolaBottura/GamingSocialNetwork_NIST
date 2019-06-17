from django.test import TestCase, RequestFactory
from .views import edit_profile, signup
from django.contrib.auth.models import AnonymousUser, User
from .models import UserProfile, create_profile

"""
class UserTestCase(TestCase):

    def test_rank(self):
        UserProfile.user = models.CharField(max_length=100, default='')
        user_test = UserProfile.objects.create(user="test", game_tag="lumachino", region="euw1")

        self.assertTrue(user_test.find_my_rank())
class ViewsTestCase(TestCase):

    def test_index(self):
        resp = self.client.get('http://127.0.0.1:8000/profiles/login')
        self.assertEqual(resp.status_code, 200)
"""


class ModelTests(TestCase):
    def test_whatever_creation(self):
        user = User.objects.create_user(username='testuser', email='test@mail.com', password='12345')
        response = create_profile(user)
        self.assertTrue(response)


class ViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@mail.com', password='12345')

    def test_login(self):
        login = self.client.login(username='testuser', password='12345')
#
        self.assertTrue(login)

    def test_view(self):
        # Create an instance of a GET request.
        request = self.factory.get('/profiles/profile/edit_profile')

        request.user = self.user

        request.user.userprofile = UserProfile()

        response = edit_profile(request)

        self.assertEqual(response.status_code, 200)
