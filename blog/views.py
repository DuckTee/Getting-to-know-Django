from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import BlogPost
from .forms import BlogPostForm

class BlogPostListView(ListView):
    '''Отображает список опубликованных постов'''
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 3 # Пагинация по 3 поста на странице

    def get_queryset(self):
        '''Фильтрует только опубликованные посты'''
        return BlogPost.objects.filter(is_published=True)

class BlogPostDetailView(DetailView):
    '''Показывает детальную информацию о посте'''
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self):
        '''Автоматически увеличивает счетчик просмотров'''
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj

class BlogPostCreateView(CreateView):
    '''Создает новую запись в блоге'''
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogPostUpdateView(UpdateView):
    '''Обновляет существующую запись'''
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})

class BlogPostDeleteView(DeleteView):
    '''Удаляет запись из блога'''
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')