from django.contrib.auth import authenticate
from modules.common.exceptions import UnauthorizeException
from rest_framework_simplejwt.tokens import RefreshToken


class AuthService:
    @staticmethod
    def authenticate_user(cedula: str, password: str):
        """
        Autentica a un usuario con cédula y contraseña. Si es válido, retorna un tupla [acces_token, refresh_token].
        """
        user = authenticate(cedula=cedula, password=password)
        if user is None:
            raise UnauthorizeException()
        return AuthService.generate_tokens_for_user(user)

    @staticmethod
    def generate_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token), str(refresh)
