from django import forms
from .models import Post, NewsletterUser, Comments, Project


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'image', 'date']


class RegisterNewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('post', 'comment', 'user', 'date')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'short_description', 'description', 'address', 'image', 'is_active', 'amount_spent')
