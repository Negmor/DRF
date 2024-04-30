from rest_framework import serializers
from .models import Article, Comment
from django.utils.timezone import now


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=30)


"""class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=300)
    status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        Article.objects.create(**validated_data)"""


def check_title(value):
    if value["title"] == "fofo":
        raise serializers.ValidationError("this  name is not valid")
    return value


# show day that passed from this comment
class CommentSerializer(serializers.ModelSerializer):
    days_ago = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        # or fields = ("","","days_ago")

    def get_days_ago(self, obj):
        return (now().date() - obj.date).days





class ArticleSerializer(serializers.ModelSerializer):
    # status=serializers.BooleanField(write_only=True)
    comments=serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = ("id", "title", "text", "status", "user","comments")
        validators = [
            check_title,
        ]
        # exclude=() tamami filed ha bejoz in filed jelosh minevisim
        # read_only_fileds=["id"]

    def validate(self, attrs):
        if attrs["title"] == attrs["text"]:
            raise serializers.ValidationError("this  name is not valid")
        return attrs

    def get_comments(self,obj):
        serializer=CommentSerializer(instance=obj.comment.all(),many=True)
        return serializer.data
    # def validate_title(self,value ): #call this filed with is valid in view--serializer.is_valid
    # if value == "fofo":
    # raise serializers.ValidationError("this  name is not valid")
    # return value


