# Generated by Django 4.0.8 on 2022-10-22 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj_man', '0031_taskanswerbyexecutors_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskanswerbyexecutors',
            name='approve_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proj_man.taskapprovestatusactions', verbose_name='Статус исполненности задачи'),
        ),
    ]
