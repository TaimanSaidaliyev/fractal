from django.db import models
import os
import pathlib
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


def get_first_name(self):
    return self.first_name + ' ' + self.last_name


User.add_to_class("__str__", get_first_name)


class CommonFiles(models.Model):
    id_record = models.IntegerField(default=0, verbose_name='ID записи')
    name = models.CharField(max_length=500, blank=True, verbose_name='Название файла')
    module_name = models.ForeignKey('ModuleName', blank=True, on_delete=models.CASCADE, verbose_name='Модуль', related_name='module_common_files')
    size = models.FloatField(default=0, verbose_name='Размер файла')
    type = models.CharField(max_length=20, verbose_name='Тип файла', blank=True)
    attached_file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='Файлы', blank=True)
    icon = models.ForeignKey('FileIcon', blank=True, on_delete=models.CASCADE, verbose_name='Иконка', related_name='icon_common_files')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name='Файлы'
        verbose_name_plural='Файлы'
        ordering = ['pk']

    def __str__(self):
        return self.attached_file.name

    def file_icon(self, file_extension):
        if (file_extension == '.jpg'):
            return 'jpg_check'
        elif (file_extension == '.doc'):
            return 'word_check'
        else:
            return 'nothing'

    @property
    def file_parameters(self):
        try:
            file_size = os.path.getsize("media/" + str(self.attached_file))
            file_name = os.path.basename("media/" + str(self.attached_file))
            file_extension = pathlib.Path(file_name).suffix
        except:
            file_size = 0
            file_name = 0
            file_extension = 1

        context = {
            'file_size': file_size,
            'file_name': file_name,
            'file_extension': file_extension,
            'media_url': settings.MEDIA_URL,
            'icon': self.file_icon(file_extension)
        }
        return context


class ModuleName(models.Model):
    module_name = models.CharField(max_length=100, verbose_name='Техническое название модуля')
    title = models.CharField(max_length=100, blank=True, verbose_name='Наименование модуля')
    icon = models

    class Meta:
        verbose_name = 'Файловое хранилище для модулей'
        verbose_name_plural = 'Файловое хранилище для модулей'
        ordering = ['pk']

    def __str__(self):
        return self.title


class FileIcon(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='Наименование иконки')
    suffix = models.CharField(blank=True, max_length=100, verbose_name='Тип файла')
    icon_url = models.CharField(blank=True, max_length=100, verbose_name='Ссылка на иконку')

    class Meta:
        verbose_name = 'Иконки файлов'
        verbose_name_plural = 'Иконки файлов'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Comments(MPTTModel):
    id_record = models.IntegerField(default=0, verbose_name='ID записи')
    module_name = models.ForeignKey('ModuleName', blank=True, on_delete=models.CASCADE, verbose_name='Модуль', related_name='module_common_comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Автор', related_name='comment_author')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(max_length=300, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    status = models.BooleanField(default=True, verbose_name='Видимость')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

    def __str__(self):
        return self.description

    class MPTTMeta:
        order_insertion_by = ['created_at']


class Company(MPTTModel):
    title = models.CharField(max_length=200, verbose_name='Название компании')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(max_length=300, verbose_name='Описание компании')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    status = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компания'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['created_at']