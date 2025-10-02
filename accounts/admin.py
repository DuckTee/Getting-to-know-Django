from django.contrib import admin

from accounts.models import CustomUser


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
