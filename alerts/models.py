from django.db import models
from django.urls import reverse


class AlerstList(models.Model):
    url_name = models.CharField(max_length=100, verbose_name='Название URL')
    color = models.CharField(max_length=100, verbose_name='Цвет уведомления', blank=True)
    description = models.CharField(max_length=1000, verbose_name='Описание уведомления', blank=True)

    def my_func(self):
        return reverse('alerts', kwargs={"pk": self.pk})

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('alerts')

    class Meta:
        verbose_name = 'Уведомления'
        verbose_name_plural = 'Уведомления'
        ordering = ['-pk']
