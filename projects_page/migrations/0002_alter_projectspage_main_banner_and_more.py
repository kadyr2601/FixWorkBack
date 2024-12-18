# Generated by Django 5.1.1 on 2024-11-05 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectspage',
            name='main_banner',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='projects_page.mainbanner', verbose_name='Main Banner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='services_banner',
            field=models.ManyToManyField(blank=True, related_name='services_banner', to='projects_page.servicecard', verbose_name='Services Banner'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='single_banner_image',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='projects_page.singlebannerimage', verbose_name='Image Banner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='single_banner_video',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='projects_page.singlebannervideo', verbose_name='Video Banner'),
            preserve_default=False,
        ),
    ]
