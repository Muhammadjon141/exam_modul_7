from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Get_info, Song
from rest_framework.decorators import action
from rest_framework import status
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer

class ArtistApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Artist')
    serializer_class = ArtistSerializer    

class AlbomApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Albom')
    serializer_class = AlbomSerializer
    
class SongApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Song').filter(status='pb')
    serializer_class = SongSerializer
    
    @action(detail=False, methods=['GET', ])
    def listen(self, request, *args, **kwargs):
        song = Get_info.get_queryset('Song')
        for songs in song:
            songs.listen_count += 1
            songs.save()
        return Response(data={'listen':"all"}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        song = Get_info.get_queryset('Song').order_by('-listen_count')[:3]
        serializer = SongSerializer(song, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['GET', ])
    def null_listen(self, request, id=None, *args, **kwargs):
        song = Get_info.get_queryset('Song').filter(listen_count=0)[:3]
        serializer = SongSerializer(song, many=True)        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET', ])
    def publish(self, request, *args, **kwargs):
        song = Get_info.get_queryset('Song').filter(status='pb')
        serializer = SongSerializer(song, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET', ])
    def draft(self, request, *args, **kwargs):
        song = Get_info.get_queryset('Song').filter(status='df')
        serializer = SongSerializer(song, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET', ])
    def to_publish(self, request, *args, **kwargs):
        song = Song.objects.filter(status='df')
        for songs in song:
            songs.df_to_pb()
        # serializer = SongSerializer(song, many=True)
        return Response(data={'change':'to publish'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET', ])
    def to_draft(self, request, *args, **kwargs):
        song = Song.objects.filter(status='pb')
        for songs in song:
            songs.pb_to_df()
        # serializer = SongSerializer(song, many=True)
        return Response(data={'change':'to draft'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET', ])
    def to_draft_detail(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        song = Song.objects.get(id=id)
        song.pb_to_df()
        # serializer = SongSerializer(song, many=True)
        return Response(data={'change':'to draft detail'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET', ])
    def to_publish_detail(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        song = Song.objects.get(id=id)
        song.df_to_pb()
        # serializer = SongSerializer(song, many=True)
        return Response(data={'change':'to publish detail'}, status=status.HTTP_200_OK)