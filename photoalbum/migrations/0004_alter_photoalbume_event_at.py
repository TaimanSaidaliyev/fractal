# Generated by Django 4.0.8 on 2022-10-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0003_photoalbume_author_photoalbume_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoalbume',
            name='event_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата события'),
        ),
    ]
