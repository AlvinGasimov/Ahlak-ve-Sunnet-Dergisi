# Generated by Django 5.1.4 on 2025-02-23 08:19

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Servis Başlığı')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='service_img', verbose_name='Resim')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, verbose_name='Slug')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Servisler',
            },
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='service_img', verbose_name='Resim')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='service.service', verbose_name='Servis')),
            ],
            options={
                'verbose_name_plural': 'Servis Alt Resimleri',
            },
        ),
    ]
