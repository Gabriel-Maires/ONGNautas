from django.shortcuts import render


def blog_view(request):
    return render(request, 'blog.html')


def home_view(request):
    return render(request, 'home.html')
