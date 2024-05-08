from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .serializers import UserSerializer, ArticleSerializer, CommentSerializer,UserSerializer
from .models import Article
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .permission import BlocklistPermission, IsOwnerOrReadOnly
from rest_framework.viewsets import ViewSet,ModelViewSet
url = "https://api.binance.com/api/v3/ticker/price??symbol=BTCUSDT"


# se can write here al list from decorators
@api_view(["Get", "post"])
def hello_world(request):
    product = [
        {
            "name": "mobile",
            "price": "13000"
        }
    ]
    return Response(product)


class Helloworld(APIView):
    ## daryaft etelaat az url
    def get(self, request):
        name = request.GET.get("name")
        return Response({"massage": "hi"})

    def post(self, request):
        return Response({"massage": "hi"})


class get_crypto(APIView):

    def get(self, request):
        coin = request.GET.get("coin")
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price??symbol={coin.upper()}")
        data = response.json()
        result = {
            "symbol": data["synbol"],
            "price": data["price"]
        }

        return Response(result)


class get_user(APIView):

    def get(self, request):
        # query set data taype
        users = Article.objects.all()
        ser = ArticleSerializer(instance=Article, many=True)

        return Response(ser.data)


class ArticleListView(APIView):
    def get(self, request):
        article = Article.objects.all()
        sery = ArticleSerializer(instance=article, many=True,context={"request":request})

        return Response(sery.data)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        INSTANSE = Article.objects.get(id=pk)
        sery = ArticleSerializer(instance=INSTANSE)

        return Response(sery.data)


class ArticleAddView(APIView):
    # permission_classes = [IsAuthenticated]
    # USE JUST FOR THIS VIEW
    permission_classes = [BlocklistPermission]

    def post(self, request):
        sery = ArticleSerializer(data=request.data, context={"request": request})
        if sery.is_valid():
            if request.user.is_authenticated:
                sery.validated_data["user"] = request.user
            sery.save()
            return Response({"response": "done"}, status=status.HTTP_201_CREATED)
        return Response(sery.errors, status=400)


class ArticleUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        instance = Article.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        serializer = ArticleSerializer(instance=instance, data=request.data, partial=True)
        # sserializer.update()
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "updated"})
        return Response(serializer.errors)

    def delete(self, request, pk):
        instance = Article.objects.get(id=pk)
        instance.delete()
        return Response({"response": "deleted"})


class CheckToken(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        return Response({"user": user.username}, status=status.HTTP_200_OK)

class ArticleCommentView(APIView):
    def get(self,request,pk):
        comments=Article.objects.get(id=pk).comment.all()
        serializer= CommentSerializer(instance=comments,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsereDetailView(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer = UserSerializer(instance=user,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



"""class ArticleViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        queryset=Article.objects.all()
        serializer=ArticleSerializer(instance=queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self,request,pk=None):
        instance = Article.objects.all()
        serializer = ArticleSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        sery = ArticleSerializer(data=request.data, context={"request": request})
        if sery.is_valid():
            sery.validated_data["user"] = request.user
            sery.save()
            return Response({"response": "done"}, status=status.HTTP_201_CREATED)
        return Response(sery.errors, status=400)

    def update(self,request,pk=None):
        instance = Article.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        serializer = ArticleSerializer(instance=instance, data=request.data, partial=True)
        # sserializer.update()
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "updated"})
        return Response(serializer.errors)"""


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


