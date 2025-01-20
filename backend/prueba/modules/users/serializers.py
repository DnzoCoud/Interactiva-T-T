from modules.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["cedula", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
