# Generated by Django 5.1.4 on 2025-02-05 13:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='about_img', verbose_name='Resim')),
                ('video', models.FileField(upload_to='about_video', verbose_name='Video')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Hakkımızda',
            },
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Galeri Başlığı')),
                ('image', models.ImageField(upload_to='galery_img', verbose_name='Resim')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Galeri',
            },
        ),
        migrations.CreateModel(
            name='GeneralItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Genel Bilgi Başlığı')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('nav_img', models.ImageField(upload_to='nav_img', verbose_name='Navigasyon Resmi')),
                ('footer_img', models.ImageField(upload_to='footer_img', verbose_name='Footer Resmi')),
                ('favicon_img', models.ImageField(blank=True, null=True, upload_to='favicon_img', verbose_name='Favicon Resmi')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook Linki')),
                ('twitter', models.URLField(blank=True, max_length=600, null=True, verbose_name='Twitter Linki')),
                ('instagram', models.URLField(blank=True, max_length=600, null=True, verbose_name='İnstagram Linki')),
                ('youtube', models.URLField(blank=True, max_length=600, null=True, verbose_name='Youtube Linki')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Genel Bilgiler',
            },
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Slider Başlığı')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='slider_img', verbose_name='Slider Resmi')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Ana Sayfa Sliderları',
            },
        ),
        migrations.CreateModel(
            name='IslamCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Şart Başlığı')),
                ('image', models.ImageField(upload_to='condition_img', verbose_name='Resim')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'İslamın Şartları',
            },
        ),
        migrations.CreateModel(
            name='PageBunner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Banner için başlık')),
                ('about_title', models.CharField(max_length=200, verbose_name='Hakkımızda banner Başlığı')),
                ('about_img', models.ImageField(upload_to='banner', verbose_name='Hakkımızda banner resim')),
                ('service_title', models.CharField(max_length=200, verbose_name='Hizmetler banner Başlığı')),
                ('service_img', models.ImageField(upload_to='banner', verbose_name='Hizmetler banner resim')),
                ('service_detail_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Hizmet Detayları banner Başlığı')),
                ('service_detail_img', models.ImageField(upload_to='banner', verbose_name='Hizmet Detayları banner resim')),
                ('blog_title', models.CharField(max_length=200, verbose_name='Bloglar banner Başlığı')),
                ('blog_img', models.ImageField(upload_to='banner', verbose_name='Bloglar banner resim')),
                ('blog_detail_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Blog Detayları banner Başlığı')),
                ('blog_detail_img', models.ImageField(upload_to='banner', verbose_name='Blog Detayları banner resim')),
                ('galery_title', models.CharField(max_length=200, verbose_name='Galeri banner Başlığı')),
                ('galery_img', models.ImageField(upload_to='banner', verbose_name='Galeri banner resim')),
                ('contact_title', models.CharField(max_length=200, verbose_name='İletişim banner Başlığı')),
                ('contact_img', models.ImageField(upload_to='banner', verbose_name='İletişim banner resim')),
                ('error_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Error banner Başlığı')),
                ('error_img', models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Error banner resim')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Sayfa Bannerları',
            },
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='SEO Başlığı')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('keywords', models.TextField(verbose_name='Anahtar Kelimeler')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('og_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Open Graph Başlığı')),
                ('og_description', models.TextField(blank=True, null=True, verbose_name='Open Graph Açıklaması')),
                ('og_image', models.ImageField(blank=True, null=True, upload_to='seo_images/', verbose_name='Open Graph Görseli')),
                ('twitter_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter Kart Başlığı')),
                ('twitter_description', models.TextField(blank=True, null=True, verbose_name='Twitter Kart Açıklaması')),
                ('twitter_image', models.ImageField(blank=True, null=True, upload_to='seo_images/', verbose_name='Twitter Kart Görseli')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'SEO Bilgileri',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Statistik Bilgi Başlığı')),
                ('value', models.IntegerField(verbose_name='Statistik Değer')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'İstatistik Bilgileri',
            },
        ),
        migrations.CreateModel(
            name='StatisticInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Bilgi Başlığı')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('image', models.ImageField(upload_to='statistic_img', verbose_name='Resim')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'İstatistik için genel bilgiler',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Aboneler',
            },
        ),
    ]
