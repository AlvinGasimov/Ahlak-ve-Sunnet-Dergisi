# Generated by Django 5.1.4 on 2025-03-04 13:23

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_tr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_ar', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_kk', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_img', verbose_name='Resim')),
                ('video', models.FileField(blank=True, null=True, upload_to='about_video', verbose_name='Video')),
            ],
            options={
                'verbose_name_plural': 'Hakkımızda',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='DynamicPage',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=200, null=True, verbose_name='Sayfa Adı')),
                ('title_tr', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=200, null=True, verbose_name='Sayfa Adı')),
                ('title_ar', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=200, null=True, verbose_name='Sayfa Adı')),
                ('title_kk', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=200, null=True, verbose_name='Sayfa Adı')),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='dynamic_page_banner', verbose_name='Banner')),
                ('content', ckeditor.fields.RichTextField(blank=True, help_text='İçerik tercüme olunamlıdır eğer diğer dillerde varsa. Default dil türkçedir', null=True, verbose_name='İçerik')),
                ('content_tr', ckeditor.fields.RichTextField(blank=True, help_text='İçerik tercüme olunamlıdır eğer diğer dillerde varsa. Default dil türkçedir', null=True, verbose_name='İçerik')),
                ('content_ar', ckeditor.fields.RichTextField(blank=True, help_text='İçerik tercüme olunamlıdır eğer diğer dillerde varsa. Default dil türkçedir', null=True, verbose_name='İçerik')),
                ('content_kk', ckeditor.fields.RichTextField(blank=True, help_text='İçerik tercüme olunamlıdır eğer diğer dillerde varsa. Default dil türkçedir', null=True, verbose_name='İçerik')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'Dinamik Sayfalar',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Galeri Başlığı')),
                ('image', models.ImageField(upload_to='galery_img', verbose_name='Resim')),
            ],
            options={
                'verbose_name_plural': 'Galeri',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='GeneralItem',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Ismi')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Ismi')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Ismi')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Ismi')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_tr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_ar', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_kk', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('nav_img', models.ImageField(blank=True, null=True, upload_to='nav_img', verbose_name='Navigasyon Resmi')),
                ('footer_img', models.ImageField(blank=True, null=True, upload_to='footer_img', verbose_name='Footer Resmi')),
                ('favicon_img', models.ImageField(blank=True, null=True, upload_to='favicon_img', verbose_name='Favicon Resmi')),
            ],
            options={
                'verbose_name_plural': 'Genel Bilgiler',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Slider Başlığı')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Slider Başlığı')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Slider Başlığı')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Slider Başlığı')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_tr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_ar', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_kk', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider_img', verbose_name='Slider Resmi')),
            ],
            options={
                'verbose_name_plural': 'Ana Sayfa Sliderları',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='IslamCondition',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Şart Başlığı')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Şart Başlığı')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Şart Başlığı')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Şart Başlığı')),
                ('image', models.ImageField(blank=True, null=True, upload_to='condition_img', verbose_name='Resim')),
            ],
            options={
                'verbose_name_plural': 'İslamın Şartları',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='NavbarItem',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=100, null=True, verbose_name='Başlık')),
                ('title_tr', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=100, null=True, verbose_name='Başlık')),
                ('title_ar', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=100, null=True, verbose_name='Başlık')),
                ('title_kk', models.CharField(blank=True, help_text='Diller için tercüme yapın.', max_length=100, null=True, verbose_name='Başlık')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('order', models.IntegerField(default=0, verbose_name='Sıra')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif mi?')),
                ('position', models.CharField(blank=True, choices=[('both', 'Her ikisi'), ('navbar', 'Navbar'), ('footer', 'Footer')], default='both', max_length=30, null=True, verbose_name='Menyu yeri')),
            ],
            options={
                'verbose_name_plural': 'Navigasyon Menüsü',
                'ordering': ['order'],
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='PageBanner',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('page', models.CharField(blank=True, choices=[('home', 'Ana Sayfa'), ('about', 'Hakkımızda'), ('service', 'Hizmetler'), ('service_detail', 'Hizmet Detayları'), ('blog', 'Makaleler'), ('blog_detail', 'Makele Detayları'), ('playlist', 'Oynatma Listeleri'), ('video', 'Videolar'), ('video_detail', 'Video Detayları'), ('galery', 'Galeri'), ('contact', 'İletişim'), ('error', 'Error')], max_length=20, null=True, unique=True, verbose_name='Sayfa')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner Başlığı')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner Başlığı')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner Başlığı')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner Başlığı')),
                ('image', models.ImageField(blank=True, help_text='Ana Sayfa, Videoalr ve detay sayfaları için boş bırakınız.', null=True, upload_to='banner', verbose_name='Banner Resmi')),
            ],
            options={
                'verbose_name_plural': 'Sayfa Bannerları',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sosyal Medya Başlığı')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('icon', models.CharField(blank=True, help_text='Font Awesome icon class ismi kullanınız. Mesela (fa-brands fa-facebook)', max_length=200, null=True, verbose_name='Icon')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Aktif mi?')),
            ],
            options={
                'verbose_name_plural': 'Sosyal Medya',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Statistik Bilgi Başlığı')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Statistik Bilgi Başlığı')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Statistik Bilgi Başlığı')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Statistik Bilgi Başlığı')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Statistik Değer')),
            ],
            options={
                'verbose_name_plural': 'İstatistik Bilgileri',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='StatisticInfo',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bilgi Başlığı')),
                ('title_tr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bilgi Başlığı')),
                ('title_ar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bilgi Başlığı')),
                ('title_kk', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bilgi Başlığı')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_tr', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_ar', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('description_kk', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açıklama')),
                ('image', models.ImageField(blank=True, null=True, upload_to='statistic_img', verbose_name='Resim')),
            ],
            options={
                'verbose_name_plural': 'İstatistik için genel bilgiler',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Aboneler',
            },
            bases=('base.datemodel',),
        ),
        migrations.CreateModel(
            name='MetaTag',
            fields=[
                ('datemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.datemodel')),
                ('name', models.CharField(blank=True, choices=[('author', 'Yazar'), ('description', 'Açıklama'), ('keywords', 'Anahtar Kelimeler'), ('robots', 'Robots'), ('viewport', 'Viewport'), ('og:title', 'Open Graph Başlığı'), ('og:description', 'Open Graph Açıklaması'), ('og:image', 'Open Graph Görseli'), ('twitter:title', 'Twitter Başlığı'), ('twitter:description', 'Twitter Açıklaması'), ('twitter:image', 'Twitter Görseli')], help_text='Meta adı veya özelliği', max_length=50, null=True)),
                ('content', models.TextField(blank=True, help_text='Meta tag içeriği (content)', null=True)),
                ('slug', models.SlugField(blank=True, help_text='Otomatik oluşturulur. Boş bırakınız.', null=True)),
                ('page_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meta_tags', to='base.navbaritem')),
            ],
            options={
                'verbose_name_plural': 'SEO',
            },
            bases=('base.datemodel',),
        ),
    ]
