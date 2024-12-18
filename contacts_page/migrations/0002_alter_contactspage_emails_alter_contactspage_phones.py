# Generated by Django 5.1.1 on 2024-11-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactspage',
            name='emails',
            field=models.ManyToManyField(blank=True, to='contacts_page.email', verbose_name='Emails'),
        ),
        migrations.AlterField(
            model_name='contactspage',
            name='phones',
            field=models.ManyToManyField(blank=True, to='contacts_page.phone', verbose_name='Phones'),
        ),
    ]
