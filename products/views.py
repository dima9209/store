from django.shortcuts import render
from products.models import ProductCategory, Product, Basket
from users.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


def products(request, category_id=None, page_number=1):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    page_per = 3
    paginator = Paginator(product, page_per)
    product_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'products': product_paginator,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
