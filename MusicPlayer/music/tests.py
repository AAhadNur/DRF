from rest_framework.views import status
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from music.models import Song, Album
from music.serializers import SongSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_album(album_name="", creator=""):
        if album_name != "" and creator != "":
            album = Album.objects.create(
                album_name=album_name,
                creator=creator
            )
            return album

    @staticmethod
    def create_song(title="", artist="", album=None, release_date=None):
        if title != "" and artist != "":
            Song.objects.create(
                title=title,
                album=album,
                artist=artist,
                release_date=release_date
            )

    def setUp(self):
        # add test data
        a1 = self.create_album("Five Star", "Sean Paul")
        self.create_song("like glue", "sean paul", a1)
        a2 = self.create_album("No Name", "Konshens")
        self.create_song("simple song", "konshens", a2)
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("all-songs", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Song.objects.all()
        print(expected)
        serialized = SongSerializer(expected, many=True)
        for info in serialized.data:
            print(
                f"Title = {info['title']}\tAlbum = {info['album']}\tArtist = {info['artist']}\tReleased = {info['release_date']}\t")
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
