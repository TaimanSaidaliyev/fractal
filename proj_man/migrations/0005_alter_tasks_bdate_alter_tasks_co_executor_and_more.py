# Generated by Django 4.0.8 on 2022-10-07 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj_man', '0004_tasks_level_tasks_lft_tasks_rght_tasks_tree_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='bdate',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='co_executor',
            field=models.ManyToManyField(blank=True, null=True, related_name='co_executor', to=settings.AUTH_USER_MODEL, verbose_name='Со-исполнители'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='edate',
            field=models.DateField(blank=True, null=True, verbose_name='Срок'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Priority', to='proj_man.priority', verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='related_tasks',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_tasks_for', to='proj_man.tasks', verbose_name='Связанные задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='proj_man.status', verbose_name='Стаус'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='tdate',
            field=models.DateField(blank=True, null=True, verbose_name='Фактическая дата выполнения'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='viewers',
            field=models.ManyToManyField(blank=True, null=True, related_name='viewers', to=settings.AUTH_USER_MODEL, verbose_name='Наблюдатели'),
        ),
    ]
