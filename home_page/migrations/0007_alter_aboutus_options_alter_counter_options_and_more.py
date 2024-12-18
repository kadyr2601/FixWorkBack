# Generated by Django 5.1.1 on 2024-11-05 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_alter_servicecard_slug'),
        ('restoration_page', '0001_initial'),
        ('reviews_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us Section', 'verbose_name_plural': 'About Us Section'},
        ),
        migrations.AlterModelOptions(
            name='counter',
            options={'verbose_name': 'Counter Section', 'verbose_name_plural': 'Counter Sections'},
        ),
        migrations.AlterModelOptions(
            name='mainbanner',
            options={'verbose_name': 'Main Banner Section', 'verbose_name_plural': 'Main Banner Section'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Partner Section', 'verbose_name_plural': 'Partners Sections'},
        ),
        migrations.AlterModelOptions(
            name='servicecard',
            options={'verbose_name': 'Service Card Section', 'verbose_name_plural': 'Service Cards Sections'},
        ),
        migrations.AlterModelOptions(
            name='singlebannerimage',
            options={'verbose_name': 'Image Banner Section', 'verbose_name_plural': 'Image Banner Section'},
        ),
        migrations.AlterModelOptions(
            name='singlebannervideo',
            options={'verbose_name': 'Video Banner Section', 'verbose_name_plural': 'Video Banner Section'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='header_text_en',
            field=models.CharField(max_length=255, verbose_name='Header in English'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='header_text_ru',
            field=models.CharField(max_length=255, verbose_name='Header in Russian'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(upload_to='about_us_image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='text_en',
            field=models.TextField(verbose_name='Text in English'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='text_ru',
            field=models.TextField(verbose_name='Text in Russian'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='number',
            field=models.IntegerField(verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='text_en',
            field=models.CharField(max_length=255, verbose_name='Text in English'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='text_ru',
            field=models.CharField(max_length=255, verbose_name='Text in Russian'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='about_us',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.aboutus', verbose_name='About Us'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='counter_banner',
            field=models.ManyToManyField(blank=True, null=True, to='home_page.counter', verbose_name='Counter Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='main_banner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.mainbanner', verbose_name='Main Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='partners_banner',
            field=models.ManyToManyField(blank=True, null=True, to='home_page.partner', verbose_name='Partners Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='restoration_banner',
            field=models.ManyToManyField(blank=True, null=True, to='home_page.servicecard', verbose_name='Restoration Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='reviews_banner',
            field=models.ManyToManyField(blank=True, null=True, to='reviews_page.review', verbose_name='Reviews Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='services_banner',
            field=models.ManyToManyField(blank=True, null=True, related_name='services_banner', to='home_page.servicecard', verbose_name='Services Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='single_banner_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.singlebannerimage', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='single_banner_video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.singlebannervideo', verbose_name='Video Banner'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='desktop_height',
            field=models.PositiveIntegerField(default=386, verbose_name='Desktop Height'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='desktop_width',
            field=models.CharField(choices=[('100', 'Full width'), ('40', 'Half width')], default='100', max_length=3, verbose_name='Desktop Width'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='image',
            field=models.ImageField(upload_to='banner/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='mobile_height',
            field=models.PositiveIntegerField(default=250, verbose_name='Mobile Height'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(upload_to='partners/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Name of the Partner'),
        ),
        migrations.AlterField(
            model_name='servicecard',
            name='icon',
            field=models.ImageField(upload_to='service-card/', verbose_name='Service Card Icon'),
        ),
        migrations.AlterField(
            model_name='servicecard',
            name='name_en',
            field=models.CharField(max_length=256, verbose_name='Service Name in English'),
        ),
        migrations.AlterField(
            model_name='servicecard',
            name='name_ru',
            field=models.CharField(max_length=256, verbose_name='Service Name in Russian'),
        ),
        migrations.AlterField(
            model_name='servicecard',
            name='slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restoration_page.restoration', to_field='slug', verbose_name='Select Restoration'),
        ),
        migrations.AlterField(
            model_name='singlebannerimage',
            name='header_text_en',
            field=models.CharField(max_length=255, verbose_name='Header in English'),
        ),
        migrations.AlterField(
            model_name='singlebannerimage',
            name='header_text_ru',
            field=models.CharField(max_length=255, verbose_name='Header in Russian'),
        ),
        migrations.AlterField(
            model_name='singlebannerimage',
            name='image',
            field=models.ImageField(upload_to='single_banner_image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='singlebannervideo',
            name='header_text_en',
            field=models.CharField(max_length=255, verbose_name='Header in English'),
        ),
        migrations.AlterField(
            model_name='singlebannervideo',
            name='header_text_ru',
            field=models.CharField(max_length=255, verbose_name='Header in Russian'),
        ),
        migrations.AlterField(
            model_name='singlebannervideo',
            name='video',
            field=models.FileField(upload_to='single_banner_video', verbose_name='Video'),
        ),
    ]
