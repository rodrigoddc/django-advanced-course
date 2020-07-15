from django.db import models
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videos:video_render', args=(self.slug, ))
