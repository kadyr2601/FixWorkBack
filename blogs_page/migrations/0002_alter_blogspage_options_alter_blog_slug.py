# Generated by Django 5.1.1 on 2024-11-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogspage',
            options={'verbose_name': 'Blogs Page Widget', 'verbose_name_plural': 'Blogs Page Widgets'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, default=1, max_length=512, unique=True, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
