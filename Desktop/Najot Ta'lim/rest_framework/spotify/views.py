from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer
from .models import Albom, Artist, Song

class ArstistApiView(APIView):
    def get(self, request):
        query_set = Artist.get_info_artist()
        serializers = ArtistSerializer(query_set, many=True)
        return Response(data=serializers.data)
    
class AlbomApiView(APIView):
    def get(self, request):
        query_set = Albom.get_info_albom()
        serializers = AlbomSerializer(query_set, many=True)
        return Response(data=serializers.data)
    
class SongApiView(APIView):
    def get(self, request):
        query_set = Song.get_info_song()
        serializers = SongSerializer(query_set, many=True)
        return Response(data=serializers.data)