from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from hrm1.models import Users

class UsersSerializer(serializers.ModelSerializer):
    name= serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)
    ranking= serializers.FloatField(required=False)

    class Meta:
        model = Users
        #fields =('name','employee_id')
        fields= '__all__'
