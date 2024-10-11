# Generated by Django 5.1.1 on 2024-10-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_banner_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebanner',
            name='page',
            field=models.CharField(choices=[('home', 'Home'), ('projects', 'Projects'), ('portfolio', 'Portfolio'), ('reviews', 'Reviews'), ('blog', 'Blog')], default='home', max_length=20),
        ),
    ]
