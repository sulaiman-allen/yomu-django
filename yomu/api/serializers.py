from rest_framework import serializers
from api.models import Album

class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    # artists = ArtistSerializer(many=True)
    class Meta:
        model = Album
        fields = ('id', 'url', 'title', 'artist', 'playlist', 'rfid')

        lookup_field = 'rfid'
        extra_kwargs = {
            'url': {'lookup_field': 'rfid'}
        }
