from pydantic import ValidationError as PydanticValidationError
from modules.users.dtos import UserCreateDto
from rest_framework import status
from modules.users.serializers import UserSerializer
from modules.users.services import UserService
from modules.common.views import BaseAPIView
from modules.common.exceptions import ResourceNotFoundException
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class UserView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE", "GET"]:
            return [IsAuthenticated()]
        return [AllowAny()]

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

        try:
            new_user_dto = UserService.create_user(dto_data)
            serializer = UserSerializer(new_user_dto.model_dump())
            return self.success_response(
                data={"user": serializer.data}, status_code=status.HTTP_201_CREATED
            )
        except ResourceNotFoundException as rnfex:
            return self.error_response(
                message=rnfex.message,
                error=rnfex.message,
                status_code=rnfex.code_status,
            )
        except Exception as ex:
            return self.error_response(
                message="Error al registrar el usuario", error=str(ex)
            )
