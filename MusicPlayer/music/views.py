from rest_framework import generics

from music.models import Song
from music.serializers import SongSerializer


class ListSongView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
