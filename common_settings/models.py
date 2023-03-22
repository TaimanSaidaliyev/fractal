from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.conf import settings


class UserTemplate(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    template_type = models.ForeignKey('TemplateType', on_delete=models.PROTECT, blank=True, verbose_name='Общий дизайн')
    sidebar = models.ForeignKey('SideBarType', on_delete=models.PROTECT, blank=True, verbose_name='Боковая панель')
    header = models.ForeignKey('HeaderType', on_delete=models.PROTECT, blank=True, verbose_name='Шапка')
    content_type = models.ForeignKey('ContentType', on_delete=models.PROTECT, blank=True, verbose_name='Тип контента')
    is_sidebar = models.ForeignKey('IsSidebar', on_delete=models.PROTECT, blank=True, verbose_name='Наличие бокового меню')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='img/common/%Y/%m/%d', verbose_name='Изображение', blank=True)
    logo_light = models.ImageField(upload_to='img/common/%Y/%m/%d', verbose_name='Логотип для светлой темы', blank=True)
    logo_dark = models.ImageField(upload_to='img/common/%Y/%m/%d', verbose_name='Логотип для темный темы', blank=True)
    background_theme = models.ImageField(upload_to='img/common/%Y/%m/%d', verbose_name='Изображение на фон', blank=True)

    def my_func(self):
        return reverse('interface', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('interface')

    class Meta:
        verbose_name = 'Общий дизайн'
        verbose_name_plural = 'Общий дизайн'
        ordering = ['-created_at']


class TemplateType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    template_style = models.CharField(max_length=100, verbose_name='Стиль')
    photo = models.ImageField(upload_to='design/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Интерфейс'
        verbose_name_plural = 'Интерфейс'
        ordering = ['-pk']


class SidebarType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    sidebar_style = models.CharField(max_length=100, verbose_name='Стиль')
    photo = models.ImageField(upload_to='design/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Боковая панель'
        verbose_name_plural = 'Боковая панель'
        ordering = ['-pk']


class IsSidebar(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    is_sidebar_top = models.CharField(max_length=100, verbose_name='Стиль шапки', blank=True)
    is_sidebar_left = models.CharField(max_length=100, verbose_name='Стиль бокового меню', blank=True)
    photo = models.ImageField(upload_to='design/%Y/%m/d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наличие бокового меню'
        verbose_name_plural = 'Наличие бокового меню'
        ordering = ['-pk']


class HeaderType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    header_style = models.CharField(max_length=100, verbose_name='Стиль')
    photo = models.ImageField(upload_to='design/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапка'
        ordering = ['-pk']


class ContentType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content_style = models.CharField(max_length=100, verbose_name='Стиль')
    photo = models.ImageField(upload_to='design/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
        ordering = ['-pk']
