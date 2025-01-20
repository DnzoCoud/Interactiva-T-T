from pydantic import ValidationError as PydanticValidationError
from modules.users.dtos import UserCreateDto
from rest_framework import status
from modules.users.serializers import UserSerializer
from modules.users.services import UserService
from modules.common.views import BaseAPIView


# Create your views here.
class UserView(BaseAPIView):
    def get(self, request):
        users = UserService.get_all()
        serializer = UserSerializer(users, many=True)
        return self.success_response(data={"users": serializer.data})

    def post(self, request):
        try:
            dto_data = UserCreateDto(**request.data)
        except PydanticValidationError as e:
            return self.error_response(
                error={"errors": e.errors()}, status_code=status.HTTP_400_BAD_REQUEST
            )

        new_user_dto = UserService.create_user(dto_data)
        serializer = UserSerializer(data=new_user_dto.model_dump())
        if serializer.is_valid():
            return self.success_response(data={"user": serializer.data})
        return self.error_response(
            message="Error al registrar el usuario", error=serializer.errors
        )
