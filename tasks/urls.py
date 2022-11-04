from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('test/', views.my_view, name='tests'),
    path('interface/', views.interface, name='interface'),
    path('delete<str:pk>/', views.deleteword, name='deleteword'),
]