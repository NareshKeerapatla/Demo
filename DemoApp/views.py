from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import  Response
from .serializers import Hello
from rest_framework import status
class MY(APIView):
    def get(self,request,format=None):
        languages=['python']
        return Response({'lang':languages})


    def post(self,request):
        serializer=Hello(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            email=serializer.data.get('email')
            msg="hello {0},your mail id {1}".format(name,email)
            return  Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
