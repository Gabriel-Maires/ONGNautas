from django.contrib.auth import forms
from authentication.models import User


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):

        model = User
