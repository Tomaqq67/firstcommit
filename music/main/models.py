from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=500, unique=True)
    runame = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.runame


class Artist(models.Model):
    name = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='artists/', null=True)
    def __str__(self):
        return self.name
    

class Track(models.Model):
    title = models.CharField(max_length = 500, unique = True)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, null=True)
    def __str__(self):
        return self.title
