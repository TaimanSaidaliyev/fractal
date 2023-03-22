# Generated by Django 4.0.8 on 2022-10-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-created_at'], 'verbose_name': 'Комментарии', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AddField(
            model_name='comments',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]