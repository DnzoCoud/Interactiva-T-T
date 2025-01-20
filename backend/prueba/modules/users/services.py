from modules.users.dtos import UserCreateDto, UserResponseDto
from modules.users.models import User
from django.db import transaction
from modules.common.exceptions import ResourceNotFoundException


class UserService:

    @staticmethod
    @transaction.atomic
    def create_user(data: UserCreateDto) -> UserResponseDto:
        if UserService.exist_cedula(data.cedula):
            raise ResourceNotFoundException("Ya existe un usuario con esta cedula")
        if UserService.exist_username(data.username):
            raise ResourceNotFoundException(
                "Ya existe un usuario con este nombre de usuario"
            )

        user = User.objects.create_user(
            cedula=data.cedula, username=data.username, password=data.cedula
        )
        return UserResponseDto(id=user.id, cedula=user.cedula, username=user.username)

    @staticmethod
    def get_all():
        users = User.objects.all().values("id", "cedula", "username")
        return [UserResponseDto(**user) for user in users]

    @staticmethod
    def exist_cedula(cedula: str) -> bool:
        return User.objects.filter(cedula=cedula).exists()

    @staticmethod
    def exist_username(username: str) -> bool:
        return User.objects.filter(username=username).exists()
