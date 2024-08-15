from django.contrib import admin
from .models import Albom, Artist, Song

admin.site.register(Albom)
admin.site.register(Artist)
admin.site.register(Song)