from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.contrib.auth.models import User
from .serializers import UserSerializer

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
        users = User.objects.all()
        ser = UserSerializer(instance=users, many=True)

        return Response(ser.data)
