from django.test import TestCase
from django.utils import timezone

from authentication.models import User
from authentication.forms import RegisterForm


class RegisterFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@gmail.com',
            'cpf': '12345678900',
            'cep': '12345678',
            'birthdate': timezone.now(),
            'address': 'test street',
            'complement': 'house 1',
            'password': 'Test@123',
            'check': 'VS'
        }

    def setUp(self):
        self.register_form: RegisterForm = RegisterForm(self.data)

    def test_if_register_form_is_creating_user(self):
        """
        Tests if register form is creating user
        """

        if self.register_form.is_valid():
            user: User = self.register_form.save()
        
        _user: User = User.objects.get(email=self.data.get('email'))

        self.assertIsNotNone(user)
        self.assertIsNotNone(_user)

    def test_if_created_user_exists(self):
        """
        Tests if created user exists
        """

        if self.register_form.is_valid():
            self.register_form.save()
        user = User.objects.filter(email=self.data.get('email'))

        self.assertTrue(user.exists())

    def test_if_created_user_password_is_hashed(self):
        """
        Tests if created user password is hashed
        """
        
        if self.register_form.is_valid():
            self.register_form.save()
        
        user: User = User.objects.get(email=self.data.get('email'))

        self.assertNotEqual(user.password, self.data.get('password'))

    def test_if_created_user_password_is_valid(self):
        """
        Tests if created user password is valid
        """

        if self.register_form.is_valid():
            self.register_form.save()
        
        user: User = User.objects.get(email=self.data.get('email'))

        self.assertTrue(user.check_password(self.data.get('password')))

    def test_if_register_form_is_validating_data(self):
        """
        Tests if register form is validating data
        """

        data = {
            'first_name': 't est',
            'last_name': 'u ser',
            'email': 'test',
            'cpf': '1234r78900',
            'cep': '1234ty678',
            'birthdate': 'test',
            'password': 'test test',
            'check': 'k'
        }

        for key, value in data.items():
            register_form: RegisterForm = RegisterForm(data.copy())
            register_form.data[key] = value

            self.assertFalse(register_form.is_valid())


    def test_no_whitespaces_validator(self):
        """
        Tests no whitespaces validator
        """

        message = 'Não use espaços em branco'

        _data = self.data.copy()
        _data['first_name'] = 'tes t'
        _data['last_name'] = 'u ser'
        _data['password'] = 'Test password@1'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('first_name'))
            self.assertIn(message, register_form.errors.get('last_name'))
            self.assertIn(message, register_form.errors.get('password'))

    def test_password_special_characters_validator(self):
        """
        Test password's special characters validator
        """
        message = 'Use pelo menos um caractere especial'

        _data = self.data.copy()
        _data['password'] = 'Test1'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('password'))

    def test_password_uppercase_letters_validator(self):
        """
        Test password's uppercase letters validator
        """

        message = 'Use pelo menos uma letra MAIÚSCULA'

        _data = self.data.copy()
        _data['password'] = 'test@1'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('password'))

    def test_password_lowercase_letters_validator(self):
        """
        Test password's lowercase letters validator
        """

        message = 'Use pelo menos uma letra minúscula'

        _data = self.data.copy()
        _data['password'] = 'TEST@1'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('password'))

    def test_password_number_validator(self):
        """
        Tests password's number validator
        """

        message = 'Use pelo menos um número'

        _data = self.data.copy()
        _data['password'] = 'Test@'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('password'))

    def test_cpf_validator(self):
        """
        Tests cpf's validator
        """

        message = 'Digite um CPF válido'

        _data = self.data.copy()
        _data['cpf'] = '1234y567890'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('cpf'))

    def test_cep_validator(self):
        """
        Tests cep's validator
        """

        message = 'Digite um CEP válido'

        _data = self.data.copy()
        _data['cep'] = '123t4567'

        register_form: RegisterForm = RegisterForm(_data)
        if not register_form.is_valid():
            self.assertIn(message, register_form.errors.get('cep'))
