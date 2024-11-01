# Generated by Django 5.1.1 on 2024-10-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_service_description_remove_service_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='title',
        ),
        migrations.AddField(
            model_name='banner',
            name='title_en',
            field=models.CharField(default=1, max_length=512, verbose_name='Title in English'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='title_ru',
            field=models.CharField(default=1, max_length=512, verbose_name='Title in Russian'),
            preserve_default=False,
        ),
    ]
