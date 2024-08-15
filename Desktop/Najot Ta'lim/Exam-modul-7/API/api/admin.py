from django.contrib import admin
from .models import Artist, Albom, Song

# admin.site.register(Artist)
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    
@admin.register(Albom)
class AlbomAdmin(admin.ModelAdmin):
    list_display = ['id', "title",]
    list_display_links = ["title", ]
    search_fields = ['title',]
    
@admin.register(Song)
class AlbomAdmin(admin.ModelAdmin):
    list_display = ['id', "title",]
    list_display_links = ["title", ]
    search_fields = ['title',]