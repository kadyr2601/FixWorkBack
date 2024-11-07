# Generated by Django 5.1.1 on 2024-11-03 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=512, verbose_name='Title in Russian')),
                ('title_en', models.CharField(max_length=512, verbose_name='Title in English')),
                ('first_paragraph_ru', models.TextField(verbose_name='First paragraph in Russian')),
                ('first_paragraph_en', models.TextField(verbose_name='First paragraph in English')),
                ('second_paragraph_ru', models.TextField(verbose_name='Second paragraph in Russian')),
                ('second_paragraph_en', models.TextField(verbose_name='Second paragraph in English')),
                ('third_paragraph_ru', models.TextField(verbose_name='Third paragraph in Russian')),
                ('third_paragraph_en', models.TextField(verbose_name='Third paragraph in English')),
                ('image', models.ImageField(upload_to='blog/')),
                ('slug', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs Page',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Customer Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('home', 'Home'), ('projects', 'Projects'), ('portfolio', 'Portfolio'), ('reviews', 'Reviews'), ('blog', 'Blog'), ('contact', 'Contact')], default='home', max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='banner/')),
                ('desktop_height', models.PositiveIntegerField(default=386)),
                ('desktop_width', models.CharField(choices=[('100', 'Full width'), ('40', 'Half width')], default='100', max_length=3)),
                ('mobile_height', models.PositiveIntegerField(default=250)),
            ],
            options={
                'verbose_name': 'Main Banner',
                'verbose_name_plural': 'Main Banners',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='portfolio/')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios Page',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=512, verbose_name='Project title in Russian')),
                ('title_en', models.CharField(max_length=512, verbose_name='Project title in English')),
                ('description_ru', models.TextField(verbose_name='Project description in Russian')),
                ('description_en', models.TextField(verbose_name='Project description in English')),
                ('image', models.ImageField(upload_to='projects/')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects Page',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=256)),
                ('comment_ru', models.TextField()),
                ('comment_en', models.TextField()),
                ('image', models.ImageField(upload_to='reviews/')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews Page',
            },
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('home', 'Home'), ('projects', 'Projects'), ('portfolio', 'Portfolio'), ('reviews', 'Reviews'), ('blog', 'Blog'), ('contact', 'Contact')], default='home', max_length=20, unique=True)),
                ('title_ru', models.CharField(max_length=512, verbose_name='Title in Russian')),
                ('title_en', models.CharField(max_length=512, verbose_name='Title in English')),
                ('description_ru', models.TextField(verbose_name='Description in Russian')),
                ('description_en', models.TextField(verbose_name='Description in English')),
            ],
            options={
                'verbose_name': 'SEO',
                'verbose_name_plural': 'SEO Settings for Pages',
            },
        ),
        migrations.CreateModel(
            name='FeedbackFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='feedbacks/')),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.feedback')),
            ],
            options={
                'verbose_name': 'Feedback File',
                'verbose_name_plural': 'Feedback Files',
            },
        ),
        migrations.CreateModel(
            name='PageBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('home', 'Home'), ('projects', 'Projects'), ('portfolio', 'Portfolio'), ('reviews', 'Reviews'), ('blog', 'Blog')], default='home', max_length=20)),
                ('type', models.CharField(choices=[('video', 'Video'), ('image', 'Image')], default='image', max_length=20)),
                ('title_ru', models.CharField(blank=True, max_length=512, null=True, verbose_name='Title in Russian')),
                ('title_en', models.CharField(blank=True, max_length=512, null=True, verbose_name='Title in English')),
                ('file', models.FileField(upload_to='banner/')),
                ('button', models.BooleanField(default=False, verbose_name='Show button - "Leave an application"')),
                ('desktop_height', models.PositiveIntegerField(default=500, verbose_name='Banner height on desktop in (px)')),
                ('mobile_height', models.PositiveIntegerField(default=300, verbose_name='Banner height on mobile in (px)')),
            ],
            options={
                'verbose_name': 'Page Banner',
                'verbose_name_plural': 'Page Banners',
                'unique_together': {('page', 'type')},
            },
        ),
        migrations.CreateModel(
            name='ProjectSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=512, verbose_name='Section title in Russian')),
                ('title_en', models.CharField(max_length=512, verbose_name='Section title in English')),
                ('description_ru', models.TextField(verbose_name='Section description in Russian')),
                ('description_en', models.TextField(verbose_name='Section description in English')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.project')),
            ],
            options={
                'verbose_name': 'Project Section',
                'verbose_name_plural': 'Project Sections',
            },
        ),
    ]
