# Generated by Django 5.1.1 on 2024-10-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_pagebanner_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pagebanner',
            unique_together={('page', 'type')},
        ),
    ]
