from django.urls import path

from . import views


urlpatterns = [
    path('delete/<int:report_id>/', views.delete_report, name='delete_report'),
    path('denouncement', views.denouncement_view, name='denouncement'),
    path('transparency', views.transparency_view, name='transparency'),
]
