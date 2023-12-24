from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'name': 'Синяя куртка The North Face',
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'price': 3390,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
                'price': 2340,
                'description': 'Плотная ткань. Легкий материал.'
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
                'price': 13590,
                'description': 'Гладкий кожаный верх. Натуральный материал.'
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'price': 2890,
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
            }
        ]
    }
    return render(request, 'products.html', context)
