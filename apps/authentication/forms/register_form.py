from django import forms
from django.core.validators import EmailValidator
from authentication.models.user import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    #TODO: Method to validate the password