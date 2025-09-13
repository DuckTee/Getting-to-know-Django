from django import forms
from .models import Product


'''
Форма продукта
'''
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' # используем все файлы из модели
