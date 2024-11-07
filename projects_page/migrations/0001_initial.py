# Generated by Django 5.1.1 on 2024-11-05 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restoration_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='Image')),
                ('desktop_height', models.PositiveIntegerField(default=386, verbose_name='Desktop Height')),
                ('desktop_width', models.CharField(choices=[('100', 'Full width'), ('40', 'Half width')], default='100', max_length=3, verbose_name='Desktop Width')),
                ('mobile_height', models.PositiveIntegerField(default=250, verbose_name='Mobile Height')),
            ],
            options={
                'verbose_name': 'Main Banner Section',
                'verbose_name_plural': 'Main Banner Section',
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
            name='SingleBannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='single_banner_image', verbose_name='Image')),
                ('header_text_ru', models.CharField(max_length=255, verbose_name='Header in Russian')),
                ('header_text_en', models.CharField(max_length=255, verbose_name='Header in English')),
            ],
            options={
                'verbose_name': 'Image Banner Section',
                'verbose_name_plural': 'Image Banner Section',
            },
        ),
        migrations.CreateModel(
            name='SingleBannerVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='single_banner_video', verbose_name='Video')),
                ('header_text_ru', models.CharField(max_length=255, verbose_name='Header in Russian')),
                ('header_text_en', models.CharField(max_length=255, verbose_name='Header in English')),
            ],
            options={
                'verbose_name': 'Video Banner Section',
                'verbose_name_plural': 'Video Banner Section',
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
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='projects_page.project', verbose_name='Select Project')),
            ],
            options={
                'verbose_name': 'Project Section Block',
                'verbose_name_plural': 'Project Section Blocks',
            },
        ),
        migrations.CreateModel(
            name='ServiceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=256, verbose_name='Service Name in Russian')),
                ('name_en', models.CharField(max_length=256, verbose_name='Service Name in English')),
                ('icon', models.ImageField(upload_to='service-card/', verbose_name='Service Card Icon')),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_services', to='restoration_page.restoration', to_field='slug', verbose_name='Select Restoration')),
            ],
            options={
                'verbose_name': 'Service Card Section',
                'verbose_name_plural': 'Service Cards Sections',
            },
        ),
        migrations.CreateModel(
            name='ProjectsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_banner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_page.mainbanner', verbose_name='Main Banner')),
                ('services_banner', models.ManyToManyField(blank=True, null=True, related_name='services_banner', to='projects_page.servicecard', verbose_name='Services Banner')),
                ('single_banner_image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_page.singlebannerimage', verbose_name='Image Banner')),
                ('single_banner_video', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_page.singlebannervideo', verbose_name='Video Banner')),
            ],
            options={
                'verbose_name': 'Projects Page Widget',
                'verbose_name_plural': 'Projects Page Widgets',
            },
        ),
    ]