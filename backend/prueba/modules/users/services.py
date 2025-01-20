from modules.users.dtos import UserCreateDto, UserResponseDto
from modules.users.models import User


class UserService:
    @staticmethod
    def create_user(data: UserCreateDto) -> UserResponseDto:
        user = User.objects.create_user(
            cedula=data.cedula, username=data.username, password=data.cedula
        )
        return UserResponseDto(id=user.id, cedula=user.cedula, username=user.username)
