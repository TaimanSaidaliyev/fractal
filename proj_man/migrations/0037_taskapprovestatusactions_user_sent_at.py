# Generated by Django 4.0.8 on 2022-11-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_man', '0036_alter_project_category_alter_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskapprovestatusactions',
            name='user_sent_at',
            field=models.DateField(blank=True, null=True, verbose_name='Время исполнения задачи'),
        ),
    ]