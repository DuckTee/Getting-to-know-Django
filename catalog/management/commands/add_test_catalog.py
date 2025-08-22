from django.core.management.base import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    help = "Добавяет тестовые данные в базу данных для модуля Product"

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;")
            cursor.execute("TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")

        category1, _ = Category.objects.get_or_create(
            name="Мясная продукция", description="мясо"
        )
        category2, _ = Category.objects.get_or_create(
            name="Шоколадная продукция", description="шоколад"
        )

        products = [
            {
                "name": "Свинина",
                "description": "жареная свинка",
                "category": category1,
                "price": 1,
            },
            {
                "name": "Шоколад бабаевский",
                "description": "горький шоколад",
                "category": category2,
                "price": 2,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Продукт добавлен: {product.name}")
                )
