from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED
from .models import Product


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = 'products_list'
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products, 60*15)
    return products


def get_products_by_category(category_id):
    """Получает данные по продуктам выбранной категории из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    key = f'products_by_category_{category_id}'
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.filter(category_id=category_id)
    cache.set(key, products, 60*15)
    return products
