from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.my_view, name='tests'),
    path('', views.interface, name='interface'),
    path('delete<int:pk>/', views.deleteword, name='deleteword'),
]