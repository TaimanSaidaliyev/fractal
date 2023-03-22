# Generated by Django 4.0.8 on 2022-10-30 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0007_company'),
        ('photoalbum', '0006_photoalbume_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbume',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_photoalbum_id', to='common.company'),
        ),
        migrations.CreateModel(
            name='PhotoAlbumeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Наименование')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обноваления')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photoalbum/%Y/%m/%d', verbose_name='Изображение обложки')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photoalbume_item_author', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_photoalbum_item_id', to='common.company')),
                ('photoalbum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photoalbume_category', to='photoalbum.photoalbume')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотография',
                'ordering': ['-pk'],
            },
        ),
    ]
