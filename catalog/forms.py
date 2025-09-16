from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Product


class ProductForm(forms.ModelForm):
    '''
    Форма продукта
    '''
    class Meta:
        model = Product
        fields = '__all__'  # используем все поля из модели

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Базовая стилизация всех полей
            field.widget.attrs.update({
                'class': 'form-control mb-3',  # Bootstrap классы
                'placeholder': field.help_text or field.label.lower(),
                'autocomplete': 'off'
            })

            # Дополнительная стилизация для конкретных полей
            if field_name == 'price':
                field.widget.attrs.update({
                    'type': 'number',
                    'step': '0.01',
                    'min': '0',  # дополнительное ограничение на уровне HTML
                    'style': 'text-align: right;'
                })
            elif field_name == 'name':
                field.widget.attrs.update({
                    'maxlength': '100',
                    'required': 'required'
                })
            elif field_name == 'description':
                field.widget.attrs.update({
                    'rows': '4',
                    'class': 'form-control form-control-lg mb-3',
                    'style': 'resize: vertical;'
                })

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы ввели запрещенное название "{forbidden_word.title()}".')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise ValidationError(_('Цена не может быть отрицательной!'))

        return price
