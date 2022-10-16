from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

class Home(ListView):
    model = Post
    template_name = 'siteKlubok/index.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Myshkin klubok'
        return context

class PostsByCategory(ListView):
    template_name = 'siteKlubok/index.html'
    context_object_name = 'posts'
    paginate_by = 1
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

def index(request):
    return render(request, 'siteKlubok/index.html')

def get_category(request):
    return render(request, 'siteKlubok/category.html')

def get_post(request):
    return render(request, 'siteKlubok/post.html')
