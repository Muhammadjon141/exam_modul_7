from django.urls import path
from .views import ArstistApiView, AlbomApiView, SongApiView

urlpatterns = [
    path('artist/', ArstistApiView.as_view(), name='ArstistApiView'),
    path('albom/', AlbomApiView.as_view(), name='AlbomApiView'),
    path('song/', SongApiView.as_view(), name='SongApiView'),
]