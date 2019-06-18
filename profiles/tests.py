from django.test import TestCase, override_settings, Client
from django.contrib.auth.models import User
from .models import UserProfile
import requests


class ViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@mail.com', password='12345')

    def test_login_page_status_code(self):
        """
        Testiamo il response code della pagina di
        login che deve sempre essere 200, in quanto
        e' una delle poche pagine che possiamo
        vedere sempre.
        """
        response = self.client.get('http://127.0.0.1:8000/profiles/login/')
        self.assertEquals(response.status_code, 200)

    def test_reset_password_page_status_code(self):
        """
        Un'altra pagina che possiamo vedere da sloggati
        e' quella del reset password, che infatti
        torna 200 come response code.
        """
        response = self.client.get('http://127.0.0.1:8000/profiles/reset-password/')
        self.assertEquals(response.status_code, 200)

    def test_riot_URL_page_status_code(self):
        """
        Test sul codice di ritorno dei due URL relativi
        ai dati legati all'account di League Of Legends.
        """
        summoner_name = 'lumachino'
        my_region = 'euw1'
        APIKey = "RGAPI-a4307801-7713-4be8-a878-04569a749956"

        summoner_data_url = "https://" + my_region + \
                            ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
                            + summoner_name + "?api_key=" + APIKey

        response = requests.get(summoner_data_url)
        summoner_data = response.json()

        ID = summoner_data['id']

        ranked_data_url = "https://" + my_region + \
                          ".api.riotgames.com/lol/league/v4/entries/by-summoner/" \
                          + ID + "?api_key=" + APIKey

        response2 = requests.get(ranked_data_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)


class ModelTests(TestCase):
    """
    Controllo che tutti valori equivalenti
    a region nel database siano composti
    effettivamente da meno di 4 caratteri.
    """
    def test_region_length(self):
        for u in UserProfile.objects.all():
            self.assertLessEqual(len(u.region), 4)
