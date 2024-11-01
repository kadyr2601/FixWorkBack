# Generated by Django 5.1.1 on 2024-10-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_project_description_remove_project_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebanner',
            name='type',
            field=models.CharField(choices=[('video', 'Video'), ('image', 'Image')], default='image', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_en',
            field=models.TextField(verbose_name='Project description in English'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_ru',
            field=models.TextField(verbose_name='Project description in Russian'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=512, verbose_name='Project title in English'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title_ru',
            field=models.CharField(max_length=512, verbose_name='Project title in Russian'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='description_en',
            field=models.TextField(verbose_name='Section description in English'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='description_ru',
            field=models.TextField(verbose_name='Section description in Russian'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='title_en',
            field=models.CharField(max_length=512, verbose_name='Section title in English'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='title_ru',
            field=models.CharField(max_length=512, verbose_name='Section title in Russian'),
        ),
    ]
