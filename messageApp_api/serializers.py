from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Users
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')


class MessageSerializer(serializers.ModelSerializer):
    """Serializes a Message object"""
    class Meta:
        model = Message
        fields = ('sender', 'reciever', 'subject', 'message', 'creation_date', 'is_read')




# class MessageSerializer(serializers.ModelSerializer):
#     """Serializes a Message object"""
#     class Meta:
#         model = Message
#         fields = ('sender', 'reciever', 'subject', 'message', 'creation_date', 'is_read')