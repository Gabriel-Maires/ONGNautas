from django.urls import path

from . import views


urlpatterns = [
    path('denouncement', views.denouncement_view, name='denouncement')
]
