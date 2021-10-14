from django.shortcuts import render


def index(request):
    context = {
        'title': 'Geekshop',
        'header': 'Интернет-магазин GeekShop',
        'user': 'Иван Иванов',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop',
        'header': 'Интернет-магазин GeekShop',
        'user': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas', 'price': 6090},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340},
            {'name': 'Черные туфли на платформе с 3 парами люверсов', 'price': 13590},
        ],
        'is_promotion' : 1,
    }
    return render(request, 'products/products.html')
