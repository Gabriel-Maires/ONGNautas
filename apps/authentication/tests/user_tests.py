from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from authentication.models import User, Denouncement, Voluntary
from django.core.files.uploadedfile import SimpleUploadedFile

#user tests

class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.user_data = {
            'username': 'caio',
            'email': 'caio123@gmail.com',
            'is_voluntary': True,
            'is_supporter': False,
            'cpf': '12345678900',
            'birthdate': timezone.now(),
            'cep': '72260851',
            'address': 'qno18',
            'complement': 'casa01',
        }
    def test_create_user(self):
        user = self.User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.is_voluntary)
        self.assertFalse(user.is_supporter)
        self.assertEqual(user.cpf, self.user_data['cpf'])
        self.assertEqual(user.birthdate, self.user_data['birthdate'])
        self.assertEqual(user.complement, self.user_data['complement'])
        self.assertEqual(user.cep, self.user_data['cep'])
        self.assertEqual(user.address, self.user_data['address'])
    def test_str(self):
        user = self.User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), user.get_full_name())