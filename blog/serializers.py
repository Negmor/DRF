from rest_framework import serializers
from .models import Article


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=30)


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=300)
    status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        Article.objects.create(**validated_data)
