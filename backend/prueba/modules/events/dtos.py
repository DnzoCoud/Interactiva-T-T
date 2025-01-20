from pydantic import BaseModel, field_validator
from io import BytesIO
from PIL import Image
import base64


class EventResponseDto(BaseModel):
    name: str
    description: str
    imagen_base64: str
    capacity: int
    start_date: str
    end_date: str
    ubication: str

    @field_validator("imagen_base64")
    def validar_imagen_base64(cls, v):
        try:
            # Comprobar si la cadena tiene el prefijo correcto
            if not v.startswith("data:image"):
                raise ValueError("La cadena no es una imagen válida en Base64.")

            # Intentar decodificar la imagen
            format, imgstr = v.split(";base64,")  # Divide el formato y la cadena
            img_data = base64.b64decode(imgstr)  # Decodifica la imagen

            # Crear un archivo de imagen desde los datos decodificados
            image = Image.open(BytesIO(img_data))

            # Validar el formato de la imagen (puedes agregar más validaciones aquí)
            if image.format not in ["JPEG", "PNG", "GIF"]:
                raise ValueError(f"El formato de imagen {image.format} no es válido.")

        except Exception as e:
            raise ValueError(f"Error al procesar la imagen Base64: {e}")
        return v
