from django.test import TestCase
from django.utils import timezone

from authentication.models import User


class UserCreationTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user_data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@gmail.com',
            'cpf': '12345678900',
            'cep': '12345678',
            'birthdate': timezone.now(),
            'address': 'test street',
            'complement': 'house 1',
            'is_voluntary': False,
            'is_supporter': False,
            'password': 'test_password'
        }

    def setUp(self) -> None:
        User.objects.create_user(**self.user_data)

    def test_if_created_user_is_not_none(self):
        """
        Test if created user is not None
        """

        user: User = User.objects.get(email=self.user_data.get('email'))

        self.assertIsNotNone(user)
    
    def test_if_created_user_exists(self):
        """
        Test if created user exists
        """
        
        user: User = User.objects.filter(email=self.user_data.get('email'))
        
        self.assertTrue(user.exists())

    def test_if_user_data_is_correct(self):
        """
        Test if user data is correct
        """

        user: User = User.objects.filter(email=self.user_data.get('email')).first()

        self.assertEqual(user.first_name, self.user_data.get('first_name'))
        self.assertEqual(user.last_name, self.user_data.get('last_name'))
        self.assertEqual(user.email, self.user_data.get('email'))
        self.assertEqual(user.cpf, self.user_data.get('cpf'))
        self.assertEqual(user.cep, self.user_data.get('cep'))
        self.assertEqual(user.birthdate, self.user_data.get('birthdate').date())
        self.assertEqual(user.address, self.user_data.get('address'))
        self.assertEqual(user.complement, self.user_data.get('complement'))
        self.assertEqual(user.is_voluntary, self.user_data.get('is_voluntary'))
        self.assertEqual(user.is_supporter, self.user_data.get('is_supporter'))
        self.assertNotEqual(user.password, self.user_data.get('password'))
        self.assertTrue(user.check_password(self.user_data.get('password')))
        self.assertEqual(user.__str__(), f'{self.user_data.get("first_name")} {self.user_data.get("last_name")}')
        self.assertEqual(user.get_full_name(), f'{self.user_data.get("first_name")} {self.user_data.get("last_name")}')
