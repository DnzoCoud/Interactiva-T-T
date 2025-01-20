from modules.users.dtos import UserCreateDto, UserResponseDto, UserPatchDto
from modules.users.models import User
from django.db import transaction
from modules.common.exceptions import ResourceNotFoundException


class UserService:

    @staticmethod
    def validate_cedula_and_username(cedula: str, username: str):
        if UserService.exist_cedula(cedula):
            raise ResourceNotFoundException("Ya existe un usuario con esta cedula")
        if UserService.exist_username(username):
            raise ResourceNotFoundException(
                "Ya existe un usuario con este nombre de usuario"
            )

    @staticmethod
    @transaction.atomic
    def create_user(data: UserCreateDto) -> UserResponseDto:
        UserService.validate_cedula_and_username(data.cedula, data.username)

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

    @staticmethod
    def exist_by_id(id) -> bool:
        return User.objects.filter(pk=id).exists()

    @staticmethod
    def get_by_id(user_id: int):
        user = (
            User.objects.filter(pk=user_id).values("id", "cedula", "username").first()
        )
        if not user:
            raise ResourceNotFoundException("No existe el usuario con ese id")
        return UserResponseDto(**user)

    @staticmethod
    def update_user(user_id, dto_data: UserPatchDto):
        if not UserService.exist_by_id(user_id):
            raise ResourceNotFoundException("No existe el usuario con ese id")

        user = User.objects.get(pk=user_id)

        if dto_data.username is not None:
            if (
                UserService.exist_username(dto_data.username)
                and user.username != dto_data.username
            ):
                raise ResourceNotFoundException(
                    "Ya existe un usuario con esta nombre de usuario."
                )
            user.username = dto_data.username

        if dto_data.cedula is not None:
            if (
                UserService.exist_cedula(dto_data.cedula)
                and user.cedula != dto_data.cedula
            ):
                raise ResourceNotFoundException("Ya existe un usuario con esta cedula")
            user.cedula = dto_data.cedula

        user.save()
        return UserResponseDto(id=user.id, cedula=user.cedula, username=user.username)

    @staticmethod
    def delete_user(user_id):
        if not UserService.exist_by_id(user_id):
            raise ResourceNotFoundException("No existe el usuario con ese id")

        user = User.objects.get(pk=user_id)
        user.delete()
