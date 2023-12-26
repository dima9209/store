from django.shortcuts import render
from users.models import User
from users.forms import UserLoginForm


def login(request):
    content = {
        'title': 'Store - Авторизация',
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', content)


def registration(request):
    content = {
        'title': 'Store - Регистрация'
    }
    return render(request, 'users/register.html', content)