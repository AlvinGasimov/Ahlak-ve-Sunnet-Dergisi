# Generated by Django 5.1.4 on 2025-01-25 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_service_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
    ]
