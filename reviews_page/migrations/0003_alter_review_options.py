# Generated by Django 5.1.1 on 2024-11-05 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_page', '0002_mainbanner_singlebannerimage_singlebannervideo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Review List'},
        ),
    ]