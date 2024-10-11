# Generated by Django 5.1.1 on 2024-10-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_pagebanner_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagebanner',
            name='banner',
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='button',
            field=models.BooleanField(default=False, verbose_name='Show button - "Leave an application"'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='desktop_height',
            field=models.PositiveIntegerField(default=500, verbose_name='Banner height on desktop in (px)'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='file',
            field=models.FileField(default=1, upload_to='banner/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='mobile_height',
            field=models.PositiveIntegerField(default=300, verbose_name='Banner height on mobile in (px)'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='title_en',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Title in English'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='title_ru',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Title in Russian'),
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
    ]
