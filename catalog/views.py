from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm, ProductModerForm


class HomeView(TemplateView):
    '''Домашняя страница'''
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ContactsView(TemplateView):
    '''Страница контактов'''
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Пользователь: {name} с телефоном: {phone} Прислал следующее сообщение: {message}")


class ProductDetailView(DetailView):
    '''Детальная страница продукта'''
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    '''Контроллер для редактирования продукта'''
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать продукт'
        return context

    def get_form_class(self):
        user = self.request.user
        product = self.get_object()  # Получаем объект продукта

        # Проверяем владельца через поле owner
        if user == product.owner:
            return ProductForm

        # Проверяем права модератора
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModerForm

        raise PermissionDenied


class ProductDeleteView(DeleteView):
    '''Контроллер для удаления продукта'''
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home') # Куда перенаправлять после удаления
