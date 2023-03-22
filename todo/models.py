import pathlib

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
import os
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ToDo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    priority = models.ForeignKey('PriorityToDo', on_delete=models.CASCADE, verbose_name='Приоритет')
    description = RichTextUploadingField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    bdate = models.DateField(blank=True, verbose_name='Дата начала')
    edate = models.DateField(blank=True, verbose_name='Дата завершения')
    completed = models.BooleanField(default=False, verbose_name='Исполнено')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='Статус')
    reminder = models.BooleanField(default=False, verbose_name='Выделить')
    progress = models.IntegerField(default=0, verbose_name='Прогресс')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Автор', related_name='author_todo')
    executor = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Исполнитель', related_name='executor_todo')

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def remind_me(self):
        current_date = datetime.date.today()
        different = (self.edate - current_date).days
        if (different > 1):
            is_coming = 0
        elif (different >= 0 and different <=1):
            is_coming = 1
        else:
            is_coming = -1
        context = {
            'different': different,
            'is_coming': is_coming
        }
        return context


class Status(models.Model):
    title = models.CharField(max_length=30, verbose_name='Статус')
    color = models.CharField(max_length=30, verbose_name='Цвет статуса')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class PriorityToDo(models.Model):
    title = models.CharField(max_length=20, db_index=True, verbose_name='Приоритет')
    color = models.CharField(max_length=20, verbose_name='Цвет Bootstrap')
    color_html = models.CharField(max_length=7, verbose_name='Цвет HTML')

    def get_absolute_url(self):
        return reverse('priority', kwargs={"priority_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Приоритет'
        verbose_name_plural = 'Приоритеты'
        ordering = ['pk']


class User(models.Model):
    def __str__(self):
        return self.last_name


class Files(models.Model):
    todo_relate = models.ForeignKey('ToDo', on_delete=models.CASCADE, verbose_name='Задача')
    name = models.CharField(max_length=500, blank=True, verbose_name='Название файла')
    size = models.FloatField(default=0, verbose_name='Размер файла')
    type = models.CharField(max_length=20, verbose_name='Тип файла', blank=True)
    attached_file = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='Файлы', blank=True)
    icon = models.ForeignKey('FileIcon', blank=True, on_delete=models.CASCADE, verbose_name='Иконка')

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