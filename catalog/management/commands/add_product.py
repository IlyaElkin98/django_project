from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.management import call_command

# Предварительное удаление данных перед загрузкой
class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

# Кастомная команда для загрузки данных из фикстуры
class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'students_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))

# Кастомная команда для загрузки тестовых продуктов
class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='Молочная продукция')

        products = [
            {'name': 'Молоко', 'description': '3,2 % жирности', 'price': '100', 'created_at': '2025-01-01', 'updated_at': '2025-11-16', 'category': category},
            {'name': 'Кефир', 'description': 'Из деревни', 'price': '12', 'created_at': '2025-01-01', 'updated_at': '2025-11-17', 'category': category},
            {'name': 'Творог', 'description': 'Неизвестно кто производитель', 'price': '70', 'created_at': '2025-01-01', 'updated_at': '2025-11-08', 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))