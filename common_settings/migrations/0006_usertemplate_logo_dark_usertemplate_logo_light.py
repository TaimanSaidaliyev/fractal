# Generated by Django 4.1 on 2022-09-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_settings', '0005_remove_issidebar_is_sidebar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertemplate',
            name='logo_dark',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Логотип для темный темы'),
        ),
        migrations.AddField(
            model_name='usertemplate',
            name='logo_light',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Логотип для светлой темы'),
        ),
    ]
