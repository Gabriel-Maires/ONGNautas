from django.test import TestCase

from authentication.forms import LoginForm

class LoginFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'email': 'test@gmail.com',
            'password': 'Test@123'
        }

    def test_if_login_form_is_validation_data(self):
        """
        Tests if login form is validating data
        """

        _data = self.data.copy()
        _data['email'] = 'test'

        login_form: LoginForm = LoginForm(_data)

        self.assertFalse(login_form.is_valid())
