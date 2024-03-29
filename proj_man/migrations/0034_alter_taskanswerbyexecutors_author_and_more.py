# Generated by Django 4.0.8 on 2022-10-23 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj_man', '0033_rename_description_taskanswerbyexecutors_answer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskanswerbyexecutors',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_answer_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='taskanswerbyexecutors',
            name='task',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_answer', to='proj_man.tasks', verbose_name='Задача'),
        ),
    ]
