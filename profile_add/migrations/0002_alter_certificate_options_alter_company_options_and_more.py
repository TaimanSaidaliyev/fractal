# Generated by Django 4.1 on 2022-09-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['-pk'], 'verbose_name': 'Сертификат', 'verbose_name_plural': 'Сертификат'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-pk'], 'verbose_name': 'Компания', 'verbose_name_plural': 'Компания'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['-pk'], 'verbose_name': 'Департамент', 'verbose_name_plural': 'Департамент'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'ordering': ['-pk'], 'verbose_name': 'Пол', 'verbose_name_plural': 'Пол'},
        ),
        migrations.AlterModelOptions(
            name='honor',
            options={'ordering': ['-pk'], 'verbose_name': 'Звание', 'verbose_name_plural': 'Звание'},
        ),
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'ordering': ['-pk'], 'verbose_name': 'Должность', 'verbose_name_plural': 'Должность'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created_date'], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профиль'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-pk'], 'verbose_name': 'Статус', 'verbose_name_plural': 'Статус'},
        ),
        migrations.AddField(
            model_name='certificate',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/certificates/%Y/%m/%d', verbose_name='Изображение сертификата'),
        ),
        migrations.AddField(
            model_name='honor',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/honors/%Y/%m/%d', verbose_name='Изображение звания'),
        ),
    ]
