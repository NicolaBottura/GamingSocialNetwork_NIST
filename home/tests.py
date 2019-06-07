from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class ViewsFunctionalityTest(TestCase):
    def test_create_new_post(self):

        response = self.client.post(reverse('home:home'),
                                    data={'form': {'post': "post di prova per il testing", "user": "test",
                                                   "created": "07/06/2019", "updated": "07/06/2019"}})

        self.assertTrue(response)


class ViewsStatusCodeTest(TestCase):

    def test_login_view(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/')

        self.assertEqual(response.status_code, 200)

