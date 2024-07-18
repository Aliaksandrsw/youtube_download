from django.db import models
from django.utils.text import slugify


class AudioTrack(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='audio_tracks/')
    youtube_url = models.URLField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class VideoLoad(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='video/')
    youtube_url = models.URLField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)