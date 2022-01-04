from django.db import models

# Create your models here.

class Snippets(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default='')
    code =models.TextField()
    language =models.CharField(max_length=100)

    def __str__(self):
        return self.title