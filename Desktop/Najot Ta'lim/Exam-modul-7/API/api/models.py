from django.db import models
from django.utils import timezone
from django.apps import apps

class StatusChoise(models.TextChoices):
    Draft = 'df', 'Draft'
    Publish = 'pb', 'Public'

class Artist(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='artists/')
    birth_date = models.DateField(default=timezone.now)
    create_date = models.DateField(auto_now_add=True)
    
    def get_songs(self):
        artist = self.objects.get(id=id)
        songs = artist.songs.all()
        
    def __str__(self) -> str:
        return self.first_name
        
class Albom(models.Model):
    title = models.CharField(max_length=80, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='alboms/')
    artist = models.ManyToManyField(Artist, related_name='alboms')
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
class Song(models.Model):
    title = models.CharField(max_length=80, null=True)
    image = models.ImageField(upload_to='songs/')
    albom = models.ForeignKey(Albom, related_name='songs', on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, related_name='songs')
    listen_count = models.IntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoise.choices, default=StatusChoise.Publish)
    create_date = models.DateField(auto_now_add=True)

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()
            
    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()

    def __str__(self) -> str:
        return super().__str__()


class Get_info:
    @staticmethod
    def get_queryset(model_name):
        try:
            # Dinamik ravishda modelni olish
            model = apps.get_model('api', model_name)
            
            if model:
                # Ushbu modelning barcha obyektlarini olish
                query_set = model.objects.all()
                return query_set
            else:
                return None
        except LookupError:
            return None
        
    @staticmethod
    def get_object(model_name, id):
        try:
            # Dinamik ravishda modelni olish
            model = apps.get_model('api', model_name)
            
            if model:
                # Ushbu modelning barcha obyektlarini olish
                query_set = model.objects.get(id=id)
                return query_set
            else:
                return None
        except LookupError:
            return None