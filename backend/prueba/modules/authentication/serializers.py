from rest_framework import serializers
from django.contrib.auth import authenticate


class AuthTokenSerializer(serializers.Serializer):
    cedula = serializers.CharField()
    password = serializers.CharField()
