from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from common.models import Company


class PhotoAlbume(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='photoalbume_author')
    category = models.ForeignKey('PhotoAlbumeCategory', on_delete=models.PROTECT, null=True, blank=True, related_name='photoalbume_category')
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата обноваления')
    event_at = models.DateField(blank=True, null=True, verbose_name='Дата события')
    event_description = models.TextField(blank=True, null=True, verbose_name='Описание события')
    image = models.ImageField(upload_to='photoalbum/%Y/%m/%d', blank=True, null=True, verbose_name='Изображение обложки')
    image_thumbnail_100_75 = ImageSpecField(source='image', processors=[ResizeToFill(100, 75)], format='JPEG', options={'quality':100})
    image_thumbnail_200_150 = ImageSpecField(source='image', processors=[ResizeToFill(200, 150)], format='JPEG', options={'quality':100})
    image_thumbnail_300_200 = ImageSpecField(source='image', processors=[ResizeToFill(300, 200)], format='JPEG', options={'quality':100})
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='company_photoalbum_id')

    class Meta:
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбом'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class PhotoAlbumeItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    photoalbum = models.ForeignKey('PhotoAlbume', on_delete=models.CASCADE, null=True, blank=True, related_name='photoalbume_category')
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='photoalbume_item_author', verbose_name='Автор альбома')
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата обноваления')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='company_photoalbum_item_id')
    image = models.ImageField(upload_to='photoalbum/%Y/%m/%d', blank=True, null=True,
                              verbose_name='Изображение обложки')
    image_thumbnail_100_75 = ImageSpecField(source='image', processors=[ResizeToFill(100, 75)], format='JPEG',
                                            options={'quality': 100})
    image_thumbnail_200_150 = ImageSpecField(source='image', processors=[ResizeToFill(200, 150)], format='JPEG',
                                             options={'quality': 100})
    image_thumbnail_300_200 = ImageSpecField(source='image', processors=[ResizeToFill(300, 200)], format='JPEG',
                                             options={'quality': 100})
    image_thumbnail_1280_720 = ImageSpecField(source='image', processors=[ResizeToFill(1280, 720)], format='JPEG',
                                             options={'quality': 100})

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотография'
        ordering = ['-pk']

    def __str__(self):
        return self.image.url


class PhotoAlbumeCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='photoalbume_category_author')
    created_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата обноваления')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория фотоальбома'
        verbose_name_plural = 'Категория фотоальбома'
        ordering = ['-pk']

    def __str__(self):
        return self.title