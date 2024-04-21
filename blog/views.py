from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.contrib.auth.models import User
from .serializers import UserSerializer, ArticleSerializer
from .models  import Article

# Create your views here.

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
        sery = ArticleSerializer(instance= article , many=True)

        return Response(sery.data)


class ArticleDetailView(APIView):
    def get(self, request,pk):
        INSTANSE = Article.objects.get(id=pk)
        sery = ArticleSerializer(instance= INSTANSE)

        return Response(sery.data)

class ArticleaddView(APIView):
        def post(self, request):
            sery = ArticleSerializer(data=request.data)
            if sery.is_valid():
                sery.save()
                return Response({"response":"done"})
            return Response(sery.errors)


class ArticleUpdateView(APIView):
    def put(self,request,pk):
        instance = Article.objects.get(id=pk)
        serializer=ArticleSerializer(instance=instance,data=request.data,partial=True)
        #sserializer.update()
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "updated"})
        return Response(serializer.errors)

    def delete(self,request,pk):
        instance = Article.objects.get(id=pk)
        instance.delete()
        return Response({"response": "deleted"})

