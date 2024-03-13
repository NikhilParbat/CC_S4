from rest_framework import serializers
from .models import World
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        field = '__all__'
        