from rest_framework import serializers
from modules.events.models import Events
from rest_framework import serializers
import base64
from django.core.files.base import ContentFile


class EventSerializer(serializers.ModelSerializer):
    imagen_base64 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Events
        fields = "__all__"

    def create(self, validated_data):
        imagen_base64 = validated_data.pop("imagen_base64", None)
        evento = Events.objects.create(**validated_data)

        if imagen_base64:
            self._save_imagen_from_base64(imagen_base64, evento)

        return evento

    def update(self, instance, validated_data):
        imagen_base64 = validated_data.pop("imagen_base64", None)

        # Actualizar los campos normales
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.video = validated_data.get("video", instance.video)
        instance.panel_comentarios = validated_data.get(
            "panel_comentarios", instance.panel_comentarios
        )

        if imagen_base64:
            self._save_imagen_from_base64(imagen_base64, instance)

        instance.save()
        return instance

    def _save_imagen_from_base64(self, base64_data, evento):
        # Decodificar la imagen Base64
        format, imgstr = base64_data.split(";base64,")  # Divide el formato y la cadena
        ext = format.split("/")[-1]  # Extrae la extensión de la imagen
        img_data = base64.b64decode(imgstr)  # Decodifica la imagen

        # Crear una imagen en memoria
        image = ContentFile(
            img_data, name=f"{evento.nombre}.{ext}"
        )  # El nombre del archivo con extensión
        evento.imagen.save(image.name, image, save=True)
