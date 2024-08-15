from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    
    @staticmethod
    def get_info_artist():
        return Artist.objects.all()
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Albom(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='alboms/')
    create_date = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def get_info_albom():
        return Albom.objects.all()

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='songs/')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_info_song():
        return Song.objects.all()

    def __str__(self):
        return self.title