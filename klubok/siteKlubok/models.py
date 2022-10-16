from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_abcolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True, blank=True)
    author = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    create_ad = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name="Категория")
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_abcolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-create_ad']


