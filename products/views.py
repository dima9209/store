from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products.html', context)
