# Generated by Django 4.0.4 on 2022-05-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_views_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
