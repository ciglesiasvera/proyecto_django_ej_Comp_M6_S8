from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Book
from .forms import CustomUserCreationForm  

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 10000:
            raise forms.ValidationError('Valoración debe estar entre 0 y 10000.')
        return rating

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control custom-input-90',
        'placeholder': 'Ingrese su correo electrónico'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs['class'] = 'form-control custom-input-90'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()  
    return render(request, 'book/register.html', {'form': form})

def home(request):
    return render(request, 'book/home.html')

def input_book(request):
    return render(request, 'book/input_book.html')
