from django.shortcuts import render


def login(request):
    content = {
        'title': 'Store - Авторизация'
    }
    return render(request, 'users/login.html', content)


def register(request):
    content = {
        'title': 'Store - Регистрация'
    }
    return render(request, 'users/register.html', content)