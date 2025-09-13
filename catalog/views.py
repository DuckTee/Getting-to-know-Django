from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm

class HomeView(TemplateView):
    '''Домашняя страница'''
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

# Старый код
# def home(request):
#     products = Product.objects.all()  # Получаем все продукты
#     return render(request, 'home.html', {'products': products})

class ContactsView(TemplateView):
    '''Страница контактов'''
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}")


# Старый код
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}")
#     return render(request, 'contacts.html')

class ProductDetailView(DetailView):
    '''Детальная страница продукта'''
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# Старый код
# def product_detail(request, product_id):
    # Получаем товар по ID или возвращаем 404 ошибку
#    product = get_object_or_404(Product, id=product_id)

    # Передаем объект товара в шаблон
#    return render(request, 'product_detail.html', {'product': product})

class ProductCreateView(CreateView):
    '''Контроллер для создания нового продукта'''
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')  # Куда перенаправлять после создания

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить продукт'
        return context

class ProductUpdateView(UpdateView):
    '''Контроллер для редактирования продукта'''
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home') # Куда перенаправлять после редактирования

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать продукт'
        return context

class ProductDeleteView(DeleteView):
    '''Контроллер для удаления продукта'''
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home') # Куда перенаправлять после удаления
