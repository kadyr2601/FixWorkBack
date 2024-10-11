# Generated by Django 5.1.1 on 2024-10-07 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('home', 'Home'), ('projects', 'Projects'), ('portfolio', 'Portfolio'), ('reviews', 'Reviews'), ('blog', 'Blog'), ('contact', 'Contact')], default='home', max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='banner/')),
                ('height', models.PositiveIntegerField(default=500)),
            ],
            options={
                'verbose_name': 'Main Banner',
                'verbose_name_plural': 'Main Banners',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.project')),
            ],
            options={
                'verbose_name': 'Project Section',
                'verbose_name_plural': 'Project Sections',
            },
        ),
    ]
