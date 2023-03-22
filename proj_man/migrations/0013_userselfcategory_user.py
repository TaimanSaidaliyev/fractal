# Generated by Django 4.0.8 on 2022-10-13 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj_man', '0012_userselfcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userselfcategory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_self_category', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
