from .views import ArtistApiWeb, AlbomApiWeb, SongApiWeb
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'artist', ArtistApiWeb, basename='artist'),
router.register(r'albom', AlbomApiWeb, basename='albom'),
router.register(r'song', SongApiWeb, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]
