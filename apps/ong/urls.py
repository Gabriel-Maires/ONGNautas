from django.urls import path

from . import views

app_name = 'ong'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog/', views.blog_view, name='blog'),
]
