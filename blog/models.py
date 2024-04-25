from django.db import models
from . import serializers
# Create your models here.



class Article(models.Model):
    title=models.CharField(max_length=100,validators=serializers.chek_title)
    text=models.TextField()
    status=models.BooleanField()


    def __str__(self):
        return self.title
