# Generated by Django 5.1.4 on 2025-03-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_remove_playlist_languages_playlist_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='name',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='languages',
        ),
        migrations.AddField(
            model_name='playlist',
            name='languages',
            field=models.ManyToManyField(blank=True, help_text='Seçilmiş dillər', null=True, related_name='playlists', to='video.language'),
        ),
    ]
