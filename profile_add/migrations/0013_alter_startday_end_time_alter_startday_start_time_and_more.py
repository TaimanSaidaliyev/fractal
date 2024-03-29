# Generated by Django 4.0.8 on 2022-10-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_add', '0012_timetrackingproperties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startday',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время завершение дня'),
        ),
        migrations.AlterField(
            model_name='startday',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время начала дня'),
        ),
        migrations.AlterField(
            model_name='timetrackingproperties',
            name='end_break_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время завершения перерыва'),
        ),
        migrations.AlterField(
            model_name='timetrackingproperties',
            name='end_day_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время завершения дня по регламенту'),
        ),
        migrations.AlterField(
            model_name='timetrackingproperties',
            name='start_break_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время начала перерыва'),
        ),
        migrations.AlterField(
            model_name='timetrackingproperties',
            name='start_day_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время начала дня по регламенту'),
        ),
    ]
