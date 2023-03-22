# Generated by Django 4.0.8 on 2022-11-03 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoalbum', '0007_alter_photoalbume_company_photoalbumeitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbumeitem',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photoalbume_item_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор альбома'),
        ),
    ]