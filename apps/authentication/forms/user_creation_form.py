from django.contrib.auth import forms
from authentication.models import User


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):

        model = User
