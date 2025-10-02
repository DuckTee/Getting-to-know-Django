from django.core.management import BaseCommand

from accounts.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(email = 'pupirka@ya.ru')
        user.set_password('1234qwer')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
