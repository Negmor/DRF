from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


# se can write here al list from decorators
@api_view(["Get", "post"])
def hello_world(request):
    product=[
        {
            "name":"mobile",
            "price":"13000"
        }
    ]
    return Response(product)



class Helloworld(APIView):
    ## daryaft etelaat az url
    def get (self,request):
        name=request.GET.get("name")
        return  Response({"massage":"hi"})

    def post(self, request):
        return Response({"massage": "hi"})