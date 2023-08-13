from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
from rolepermissions.decorators import has_role_decorator

from django.contrib import messages
from django.contrib.messages import constants
from .forms import RegisterNewsletterForm


def blog_view(request):
    return render(request, 'blog.html')


def home_view(request):
    return render(request, 'home.html')


@has_role_decorator('Admin')
def create_posts(request):
    match request.method:
        case 'GET':
            if request.user.is_authenticated:
                return redirect(reverse('blog'))

            return render(request, 'blog.html')
        case 'POST':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post_form.save()
                
                messages.add_message(request, constants.SUCCESS, 'Post criado com sucesso!')


def show_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})


def show_posts_per_category(request):
    sel_posts = Post.objects.filter(category = request.POST.get('category'))
    return render(request, 'blog.html', {'sel_posts':sel_posts})


@has_role_decorator('Admin', 'Voluntary', 'Supporter')
def make_comment(request):
    pass


def newsletter_register(request):
    register_news_user = RegisterNewsletterForm()

    if register_news_user.is_valid():
        try:
            register_news_user.save()

        except:
            messages.add_message(
                        request, 
                        constants.ERROR, 
                        'Erro interno do sistema. Tente novamente mais tarde.'
                    )