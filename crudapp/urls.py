from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('edit<str:pk>/', views.edit, name='edit'),
    # path('delete<str:pk>/', views.delete, name='delete'),
]