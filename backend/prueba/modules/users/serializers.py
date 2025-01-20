from modules.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cedula = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
