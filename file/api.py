from decimal import Context
from django.http import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from .serializers import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args,**kwargs):
        serializer= self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response(token.key)

class UserList1(APIView):
    def get(self,request):
        model=Book.objects.all()
        serializer=UsersSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail1(APIView):

    def get_user(self, id):
        try:
            model=Book.objects.get(id=id)
            return model
        except Book.DoesNotExist:
            return 

    def get(self,request, id):
        if not self.get_user(id):
            return Response(f'User with {id} not found in',status=status.HTTP_404_NOT_FOUND)
        serializer=UsersSerializer(self.get_user(id))
        return Response(serializer.data)

    def put(self,request, id):
        if not self.get_user(id):
            return Response(f'User with {id} not found in',status=status.HTTP_404_NOT_FOUND)
        serializer=UsersSerializer(self.get_user(id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        model= self.get_user(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        