from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from file.models import Book

class UsersSerializer(serializers.ModelSerializer):
    title= serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    pdf= serializers.FileField(required=False)

    class Meta:
        model = Book
        #fields =('name','employee_id')
        fields= '__all__'
