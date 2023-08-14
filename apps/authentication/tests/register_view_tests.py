from django.test import TestCase
from django.test.client import Client

from django.utils import timezone

from django.urls import reverse
from django.http import HttpRequest

from django.contrib.messages import get_messages

from authentication.models import User, Voluntary


class RegisterViewTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.request: HttpRequest = HttpRequest()

        cls.data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@gmail.com',
            'cpf': '12345678901',
            'cep': '12345678',
            'birthdate': timezone.now(),
            'address': 'test street',
            'complement': 'house 1',
            'password': 'Test@123',
            'check': 'VS'
        }

    def setUp(self):
        self.client: Client = Client()

    def test_if_register_view_returns_status_code_200(self):
        """
        Test if register view returns status code 200
        """

        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)

    def test_if_register_view_not_return_status_code_404(self):
        """
        Test if register view not return status code 404
        """

        response = self.client.get(reverse('register'))

        self.assertNotEqual(response.status_code, 404)

    def test_if_register_view_render_register_template(self):
        """
        Test if register view render register template
        """
        
        response = self.client.get(reverse('register'))

        self.assertTemplateUsed(response, 'register.html')

    def test_if_register_view_not_render_another_template(self):
        """
        Test if register view not render another template
        """

        response = self.client.get(reverse('register'))

        self.assertTemplateNotUsed(response, 'login.html')

    def test_if_register_view_is_creating_user(self):
        """
        Test if register view is creating user
        """

        self.request.POST = self.data

        initial_user_count = User.objects.count()
        response = self.client.post(reverse('register'), data=self.data)
        self.assertEqual(response.status_code, 200)

        new_user_count = User.objects.count()
        self.assertEqual(new_user_count, initial_user_count + 1)

        new_user = User.objects.last()
        self.assertEqual(new_user.email, self.data.get('email'))
        self.assertEqual(new_user.first_name, self.data.get('first_name'))
        self.assertEqual(new_user.last_name, self.data.get('last_name'))
        self.assertEqual(new_user.cpf, self.data.get('cpf'))
        self.assertEqual(new_user.cep, self.data.get('cep'))
        self.assertTrue(new_user.is_voluntary)
        self.assertFalse(new_user.is_supporter)

        voluntary = Voluntary.objects.get(user=new_user)
        self.assertEqual(voluntary.hours_worked, 0.0)
