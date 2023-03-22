# Generated by Django 4.1 on 2022-09-26 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0008_newslikes_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslikes',
            name='count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='newslikes',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Поставил лайк'),
        ),
    ]
