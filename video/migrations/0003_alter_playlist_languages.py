# Generated by Django 5.1.4 on 2025-03-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_playlist_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='languages',
            field=models.CharField(blank=True, help_text='Seçilmiş dillər', max_length=255, null=True),
        ),
    ]
