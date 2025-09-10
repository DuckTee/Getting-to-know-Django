from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'home.html', {'products': products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}")
    return render(request, 'contacts.html')


def product_detail(request, product_id):
    # Получаем товар по ID или возвращаем 404 ошибку
    product = get_object_or_404(Product, id=product_id)

    # Передаем объект товара в шаблон
    return render(request, 'product_detail.html', {'product': product})
