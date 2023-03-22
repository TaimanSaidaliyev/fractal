# Generated by Django 4.0.8 on 2022-10-20 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj_man', '0023_taskchangehistoryaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskchangehistoryaction',
            options={'ordering': ['pk'], 'verbose_name': 'Сведения об изменении задачи', 'verbose_name_plural': 'Сведения об изменении задачи'},
        ),
        migrations.RemoveField(
            model_name='taskchangehistory',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='taskchangehistory',
            name='task',
        ),
        migrations.RemoveField(
            model_name='taskchangehistory',
            name='user',
        ),
        migrations.AddField(
            model_name='taskchangehistory',
            name='task_change_action',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task_change', to='proj_man.taskchangehistoryaction', verbose_name='Сведения об изменении задачи'),
            preserve_default=False,
        ),
    ]