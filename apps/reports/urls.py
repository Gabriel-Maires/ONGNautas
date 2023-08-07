from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('denouncement', views.denouncement_view, name='denouncement')
]
