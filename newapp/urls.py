from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('join/', views.join, name='join'),
]