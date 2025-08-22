from django.http import HttpResponse
from django.shortcuts import render
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
