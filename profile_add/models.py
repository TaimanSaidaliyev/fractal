from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    fathers_name = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    person_id = models.CharField(max_length=30, blank=True, default=0, verbose_name='ИИН')
    gender = models.ForeignKey('Gender', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Пол', related_name='gender')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рожения')
    start_date = models.DateField(null=True, blank=True, verbose_name='Приступил к работе')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    job_title = models.ForeignKey('JobTitle', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Должность', related_name='jobtitle')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Департамент', related_name='department')
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания', related_name='company')
    certificate = models.ManyToManyField('Certificate', blank=True, verbose_name='Сертификат', related_name='sertificate')
    honor = models.ManyToManyField('Honor', blank=True, verbose_name='Звания в компании', related_name='honor')
    education = models.CharField(max_length=100, blank=True, verbose_name='Образование')
    location = models.CharField(max_length=30, blank=True, verbose_name='Место работы')
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Статус',related_name='education')
    telephone = models.CharField(max_length=30, blank=True, verbose_name='Контактный телефон')
    telephone_job = models.CharField(max_length=30, blank=True, verbose_name='Рабочий телефон')
    skype = models.CharField(max_length=30, blank=True, verbose_name='Skype')
    instagram = models.CharField(max_length=30, blank=True, verbose_name='Instagram')
    linkedin = models.CharField(max_length=30, blank=True, verbose_name='LinkedIn')
    facebook = models.CharField(max_length=30, blank=True, verbose_name='Facebook')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Биография')
    website = models.CharField(max_length=30, blank=True, verbose_name='Веб-сайт')
    quote = models.TextField(max_length=500, blank=True, verbose_name='Цитата для блога')

    def my_func(self):
        return reverse('profile', kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)

    def get_absolute_url(self):
        return reverse('profile')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ['-created_date']


class Gender(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description =  models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
        ordering = ['-pk']


class JobTitle(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    priority_number = models.IntegerField(default=0, blank=True, null=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='jobtitle_company')
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'
        ordering = ['-pk']


class Department(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    priority = models.IntegerField(default=0, blank=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='department_company')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департамент'
        ordering = ['-pk']


class Company(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компания'
        ordering = ['-pk']



class Certificate(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='img/certificates/%Y/%m/%d', verbose_name='Изображение сертификата', blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификат'
        ordering = ['-pk']


class Honor(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='img/honors/%Y/%m/%d', verbose_name='Изображение звания', blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Звание'
        verbose_name_plural = 'Звание'
        ordering = ['-pk']


class Status(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'
        ordering = ['-pk']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class TimeTrackingProperties(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Время по регламенту')
    start_day_time = models.TimeField(blank=True, null=True, verbose_name='Время начала дня по регламенту')
    end_day_time = models.TimeField(blank=True, null=True, verbose_name='Время завершения дня по регламенту')
    start_break_time = models.TimeField(blank=True, null=True, verbose_name='Время начала перерыва')
    end_break_time = models.TimeField(blank=True, null=True, verbose_name='Время завершения перерыва')
    company = models.IntegerField(blank=True, default=0, verbose_name='Компания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Время по регламенту'
        verbose_name_plural = 'Время по регламенту'



class StartDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(verbose_name='Дата')
    start_time = models.TimeField(blank=True, null=True, verbose_name='Время начала дня')
    end_time = models.TimeField(blank=True, null=True, verbose_name='Время завершение дня')
    is_working = models.BooleanField(default=False, verbose_name='Работает')
    is_ended = models.BooleanField(default=False, verbose_name='Завершен')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание опоздания')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Рабочий день'
        verbose_name_plural = 'Рабочий день'
        ordering = ['-pk']

    @property
    def time_tracking_properties(self):
        working_time = TimeTrackingProperties.objects.get(company=1)
        today = datetime.date.today()
        fmt = "%H:%M:%S"
        ds1 = working_time.start_day_time
        ds2 = self.start_time
        context = {
            'ds1': ds1,
            'ds2': ds2,
        }
        return context


class JustTest(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Время по регламенту')
    type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Время по регламенту')

    def __str__(self):
        return self.name
