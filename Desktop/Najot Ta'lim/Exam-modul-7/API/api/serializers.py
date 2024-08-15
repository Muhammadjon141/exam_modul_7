from rest_framework import serializers
from .models import Artist, Albom, Song

        
class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ['title', 'description', 'image', 'artist', 'songs']

class ArtistSerializer_to_Song(serializers.ModelSerializer):
    alboms = AlbomSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'username', 'image', 'birth_date', 'songs', 'alboms']

class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(many=False, read_only=True)
    artist = ArtistSerializer_to_Song(many=True, read_only=True)
    class Meta:
        model = Song
        fields = ['title', 'image', 'albom', 'artist', 'listen_count', 'status']
    

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    alboms = AlbomSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'username', 'image', 'birth_date', 'songs', 'alboms']
        
    def get_songs(self, obj):
        return SongSerializer(obj.song_set.all(), many=True).data
