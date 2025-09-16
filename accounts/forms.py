from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class UserRegisterForm(forms.ModelForm):
    """Форма регистрации пользователя"""
    password1 = forms.CharField(
        label=_('Пароль'),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_('Введите надёжный пароль.')
    )
    password2 = forms.CharField(
        label=_('Подтвердите пароль'),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_('Введите тот же пароль ещё раз для подтверждения.')
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'country')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Пароли не совпадают.'))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
