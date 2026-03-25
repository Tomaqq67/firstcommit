from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=500, unique=True)
    runame = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.runame

class Track(models.Model):
    title = models.CharField(max_length = 500, unique = True)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title
