from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('home/', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('inputbook/', views.input_book, name='inputbook'),
]