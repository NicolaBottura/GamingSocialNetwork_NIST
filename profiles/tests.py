from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

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


class ViewsFunctionalityTest(TestCase):
    def test_create_new_user(self):
        response = self.client.post(reverse('profiles:signup'),
                                    data={'form': {'user': "test", "first_name": "te", "last_name": "st",
                                                   "password1": "Test1234", "password2": "Test1234",
                                                   "email": "test@mail.com"}})

        self.assertTrue(response)

    def test_login(self):
        response = self.client.login(username="testuser", password="testuser321")

        self.assertEqual(response, False)


class ViewsStatusCodeTest(TestCase):

    def test_login_view(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/profiles/login/')

        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/profiles/profile/')

        self.assertEqual(response.status_code, 200)
"""
    def test_riot_urls(self):
        client = Client()
        summoner_name = "lumachino"
        my_region = "euw1"
        APIKey = "RGAPI-6c28be85-97b4-4ed0-b4d0-023c6c817145"

        summoner_data_url = "https://" + my_region + \
                            ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
                            + summoner_name + "?api_key=" + APIKey

        response = client.get(summoner_data_url)

        self.assertEqual(response.status_code, 200)
"""