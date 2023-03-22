from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='get_news')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи', blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def my_func(self):
        return 'Hello from Model'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='comments_news')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name='Текст')
    status = models.BooleanField(verbose_name='Видимость', default=False)


class NewsLikes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='likes_new')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Поставил лайк', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0, blank=True, verbose_name='Количество')


class NewsSave(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='saved_news')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0, blank=True, verbose_name='Количество')