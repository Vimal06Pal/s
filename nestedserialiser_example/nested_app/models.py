from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length = 50)
    singer = models.ForeignKey(Singer,on_delete=CASCADE)
    durations = models.IntegerField()

    def __str__(self):
        return self.title