# Generated by Django 5.1.1 on 2024-11-05 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_delete_service'),
        ('restoration_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecard',
            name='slug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restoration_page.restoration', to_field='slug', verbose_name='Restoration'),
        ),
    ]
