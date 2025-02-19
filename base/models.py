from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

class GeneralItem(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Genel Bilgi Başlığı")
    description = RichTextField(verbose_name = "Açıklama")
    nav_img = models.ImageField(upload_to='nav_img', verbose_name = "Navigasyon Resmi")
    footer_img = models.ImageField(upload_to='footer_img', verbose_name = "Footer Resmi")
    favicon_img = models.ImageField(upload_to='favicon_img', verbose_name = "Favicon Resmi", null=True, blank=True)
    facebook = models.URLField(verbose_name = "Facebook Linki", null=True, blank=True)
    twitter = models.URLField(verbose_name = "Twitter Linki", max_length=600, null=True, blank=True)
    instagram = models.URLField(verbose_name = "İnstagram Linki", max_length=600, null=True, blank=True)
    youtube = models.URLField(verbose_name = "Youtube Linki", max_length=600, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Genel Bilgiler"     
        
        
class NavbarItem(models.Model):
    
    POSITION_CHOICES = [
        ('both', 'Her ikisi'),
        ('navbar', 'Navbar'),
        ('footer', 'Footer'),
    ]
    
    title = models.CharField(max_length=100, verbose_name="Başlık")
    url = models.CharField(max_length=200, verbose_name="URL")
    order = models.IntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    position = models.CharField(max_length=30, choices=POSITION_CHOICES, default='both', verbose_name="Menyu yeri", null=True, blank=True)
        
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Navigasyon Menüsü"

class HomeSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Slider Başlığı")
    description = RichTextField(verbose_name = "Açıklama", blank=True, null=True)
    image = models.ImageField(upload_to='slider_img', verbose_name = "Slider Resmi")
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ana Sayfa Sliderları"
        
        
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Başlık")
    description = RichTextField(verbose_name = "Açıklama")
    image = models.ImageField(upload_to='about_img', verbose_name = "Resim")
    video = models.FileField(upload_to='about_video', verbose_name = "Video")
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Hakkımızda"
        
        
class IslamCondition(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Şart Başlığı")
    image = models.ImageField(upload_to='condition_img',verbose_name='Resim')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İslamın Şartları"
        
        
class StatisticInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Bilgi Başlığı")
    description = RichTextField(verbose_name = "Açıklama")   
    image = models.ImageField(upload_to='statistic_img', verbose_name='Resim')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "İstatistik için genel bilgiler"
        
        
class Statistic(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Statistik Bilgi Başlığı")
    value = models.IntegerField(verbose_name='Statistik Değer')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İstatistik Bilgileri"
        
        
class Subscribe(models.Model):
    email = models.EmailField(verbose_name = "Email")
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Aboneler"
        
        
class Galery(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Galeri Başlığı")
    image = models.ImageField(upload_to='galery_img', verbose_name='Resim')
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galeri"
        
        
class PageBunner(models.Model):
    
    title = models.CharField(max_length=200, verbose_name = "Banner için başlık")
    
    about_title = models.CharField(max_length=200, verbose_name = "Hakkımızda banner Başlığı")
    about_img = models.ImageField(verbose_name = "Hakkımızda banner resim", upload_to='banner')
    
    service_title = models.CharField(max_length=200, verbose_name = "Hizmetler banner Başlığı")
    service_img = models.ImageField(verbose_name = "Hizmetler banner resim", upload_to='banner')
    
    service_detail_title = models.CharField(max_length=200, verbose_name = "Hizmet Detayları banner Başlığı", blank=True, null=True)
    service_detail_img = models.ImageField(verbose_name = "Hizmet Detayları banner resim", upload_to='banner')
    
    blog_title = models.CharField(max_length=200, verbose_name = "Bloglar banner Başlığı")
    blog_img = models.ImageField(verbose_name = "Bloglar banner resim", upload_to='banner')
    
    blog_detail_title = models.CharField(max_length=200, verbose_name = "Blog Detayları banner Başlığı", blank=True, null=True)
    blog_detail_img = models.ImageField(verbose_name = "Blog Detayları banner resim", upload_to='banner')
    
    galery_title = models.CharField(max_length=200, verbose_name = "Galeri banner Başlığı")
    galery_img = models.ImageField(verbose_name = "Galeri banner resim", upload_to='banner')
    
    contact_title = models.CharField(max_length=200, verbose_name = "İletişim banner Başlığı")
    contact_img = models.ImageField(verbose_name = "İletişim banner resim", upload_to='banner')
    
    error_title = models.CharField(max_length=200, verbose_name = "Error banner Başlığı", blank=True, null=True)
    error_img = models.ImageField(verbose_name = "Error banner resim", blank=True, null=True, upload_to='banner')
    
    created_at = models.DateField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    updated_at = models.DateField(auto_now=True, verbose_name = "Güncellenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sayfa Bannerları"
        
        

class MetaTag(models.Model):
    META_NAME_CHOICES = [
        ("author", "Yazar"),
        ("description", "Açıklama"),
        ("keywords", "Anahtar Kelimeler"),
        ("robots", "Robots"),
        ("viewport", "Viewport"),
        ("og:title", "Open Graph Başlığı"),
        ("og:description", "Open Graph Açıklaması"),
        ("og:image", "Open Graph Görseli"),
        ("twitter:title", "Twitter Başlığı"),
        ("twitter:description", "Twitter Açıklaması"),
        ("twitter:image", "Twitter Görseli"),
    ]
    
    page_name = models.CharField(max_length=255, help_text="Ana sayfa için boş bırakınız. Sayfa adı (örnek: Hakkımızda, Servis, Blog, Galeri, İletişim)", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(max_length=50, choices=META_NAME_CHOICES, help_text="Meta adı veya özelliği")
    content = models.TextField(help_text="Meta tag içeriği (content)")
    
    def save(self, *args, **kwargs):
        if not self.page_name:
            self.slug = ""
        if not self.slug or self.slug != slugify(self.page_name):
            self.slug = slugify(self.page_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.page_name} - {self.name}"
    
    class Meta:
        verbose_name_plural = "SEO"