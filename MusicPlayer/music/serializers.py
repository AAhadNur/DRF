from rest_framework import serializers

from music.models import Album, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'album', 'artist', 'release_date']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['album_name', 'creator']
