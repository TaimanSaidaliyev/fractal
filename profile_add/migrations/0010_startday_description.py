# Generated by Django 4.0.8 on 2022-10-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0009_startday_is_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='startday',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание опоздания'),
        ),
    ]