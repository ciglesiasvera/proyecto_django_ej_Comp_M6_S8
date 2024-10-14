from django.contrib import admin
from django.urls import path, include
from book import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),  # Esto incluye todas las URLs de la app 'book'
]
