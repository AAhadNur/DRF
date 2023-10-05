from django.db import models

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)

    class Meta:
        ordering = ['album_name']

    def __str__(self):
        return self.album_name


class Song(models.Model):
    title = models.CharField(max_length=511)
    album = models.ForeignKey(
        Album, related_name='album_songs', on_delete=models.SET_NULL, null=True)
    artist = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
