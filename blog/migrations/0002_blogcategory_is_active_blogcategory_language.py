# Generated by Django 5.1.4 on 2025-03-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Aktif mi?'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='language',
            field=models.CharField(blank=True, choices=[('tr', 'Turkish'), ('ar', 'Arabic'), ('kk', 'Kurdish')], default='tr', max_length=2, null=True, verbose_name='Dil'),
        ),
    ]
