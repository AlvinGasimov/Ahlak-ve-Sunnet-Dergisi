# Generated by Django 5.1.4 on 2025-02-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_metatag_delete_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatag',
            name='slug',
            field=models.SlugField(blank=True, help_text='Səhifənin unikal slug-u (məs: ana-səhifə, haqqimizda)', null=True, unique=True),
        ),
    ]
