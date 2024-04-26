from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title
