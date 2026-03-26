from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Отключаем стандартное поле username
    username = None

    # Делаем email обязательным полем для авторизации
    email = models.EmailField(unique=True, verbose_name='Email')

    # Аватар
    avatar = models.ImageField(
        upload_to='accounts/avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )

    # Номер телефона
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона'
    )

    # Страна
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Страна'
    )

    # Токен
    token = models.CharField(
        max_length=100,
        verbose_name='Токен',
        blank=True,
        null=True
    )

    # Указываем email как уникальное поле для входа
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
