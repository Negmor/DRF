from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BlockUser(models.Model):
    username = models.CharField(max_length=50, unique=True)


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    text = models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.text[:30]

