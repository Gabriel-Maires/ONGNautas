from django.urls import path

from . import views


urlpatterns = [
    path('denouncement', views.denouncement_view, name='denouncement'),
    path('transparency', views.transparency_view, name='transparency'),
]
