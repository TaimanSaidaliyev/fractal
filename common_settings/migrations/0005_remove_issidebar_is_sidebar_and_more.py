# Generated by Django 4.1 on 2022-09-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_settings', '0004_alter_issidebar_is_sidebar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issidebar',
            name='is_sidebar',
        ),
        migrations.AddField(
            model_name='issidebar',
            name='is_sidebar_left',
            field=models.CharField(blank=True, max_length=100, verbose_name='Стиль бокового меню'),
        ),
        migrations.AddField(
            model_name='issidebar',
            name='is_sidebar_top',
            field=models.CharField(blank=True, max_length=100, verbose_name='Стиль шапки'),
        ),
    ]