from django.urls import path
from music.views import ListSongView

urlpatterns = [
    path('songs/', ListSongView.as_view(), name='all-songs'),
]
