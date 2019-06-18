from django.test import TestCase, Client
from home.models import Post, User


class ViewTests(TestCase):
    def test_home_page_status_code(self):
        """
        Se, come in questo caso, non siamo loggati
        non ci e' permesso vedere la home e quindi
        non ritornera' 200 come response code.
        """
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertNotEquals(response.status_code, 200)


class ModelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('Test', 'test@.com', 'Test1234')

        Post.objects.create(post='just a test', user=self.user)

    def test_text_content(self):
        """
        Controllo che l'id ed il contenuto del post
        combacino
        """
        post = Post.objects.get(id=1)
        expected_object_name = post.post
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        """
        Effettuo il login in modo tale da poter
        accedere alla pagine della home e quindi poter
        vedere i vari posts, quindi controlliamo che
        abbia effettuato il login controllando
        che il response code della home sia 200.
        Dopodiche' che contenga il testo corretto
        e che renderizzi la templates giusta.
        """
        self.client.login(username='Test', password='Test1234')
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'home/home.html')


