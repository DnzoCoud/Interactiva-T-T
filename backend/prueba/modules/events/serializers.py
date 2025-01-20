from rest_framework import serializers
from modules.events.models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"
