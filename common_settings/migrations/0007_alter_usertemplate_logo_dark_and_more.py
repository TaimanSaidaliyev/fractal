# Generated by Django 4.1 on 2022-09-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_settings', '0006_usertemplate_logo_dark_usertemplate_logo_light'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertemplate',
            name='logo_dark',
            field=models.ImageField(blank=True, upload_to='img/common/%Y/%m/%d', verbose_name='Логотип для темный темы'),
        ),
        migrations.AlterField(
            model_name='usertemplate',
            name='logo_light',
            field=models.ImageField(blank=True, upload_to='img/common/%Y/%m/%d', verbose_name='Логотип для светлой темы'),
        ),
        migrations.AlterField(
            model_name='usertemplate',
            name='photo',
            field=models.ImageField(blank=True, upload_to='img/common/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
