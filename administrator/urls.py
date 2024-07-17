from django.urls import path
from . import views



urlpatterns = [
    path('', views.beranda_admin, name='beranda_admin'),
]