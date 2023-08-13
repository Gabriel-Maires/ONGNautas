from django import forms
from .models import Post, NewsletterUser


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'image', 'date']


class RegisterNewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']