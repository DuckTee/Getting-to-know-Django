from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, null=True, verbose_name='Содержимое')
    picture = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
        ordering = ['-created_at']  # Сортировка по дате создания
