from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig  # Импорт конфигурации приложения
from .views import (
    HomeView,
    ContactsView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
) # Импорт представлений


# Устанавливаем пространство имен для URL
app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),  # Детальная страница продукта

    path('product/create/', ProductCreateView.as_view(), name='product_create'), # Создание
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'), # Редактирование
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'), # Удаление

]
