from pydantic import ValidationError as PydanticValidationError
from modules.users.dtos import UserCreateDto, UserPatchDto
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
        if self.request.method in ["GET"]:
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


class UserDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = UserService.get_by_id(user_id)
            serializer = UserSerializer(user.model_dump())
            return self.success_response(
                data={"user": serializer.data}, status_code=status.HTTP_200_OK
            )
        except ResourceNotFoundException as rnfex:
            return self.error_response(
                message=rnfex.message,
                error=rnfex.message,
                status_code=rnfex.code_status,
            )
        except Exception as ex:
            return self.error_response(
                message="Error al consultar el usuario", error=str(ex)
            )

    def patch(self, request, user_id):
        try:
            dto_data = UserPatchDto(**request.data)
        except PydanticValidationError as e:
            return self.error_response(
                error={"errors": e.errors()}, status_code=status.HTTP_400_BAD_REQUEST
            )
        try:
            updated_user = UserService.update_user(user_id, dto_data)
            serializer = UserSerializer(updated_user.model_dump())
            return self.success_response(
                data={"user": serializer.data}, status_code=status.HTTP_200_OK
            )
        except ResourceNotFoundException as rnfex:
            return self.error_response(
                message=rnfex.message,
                error=rnfex.message,
                status_code=rnfex.code_status,
            )
        except Exception as ex:
            return self.error_response(
                message="Error al actualizar el usuario", error=str(ex)
            )

    def delete(self, request, user_id):
        try:
            UserService.delete_user(user_id)
            return self.success_response(
                status_code=status.HTTP_200_OK,
                message="Usuario eliminado correctamente.",
            )
        except ResourceNotFoundException as rnfex:
            return self.error_response(
                message=rnfex.message,
                error=rnfex.message,
                status_code=rnfex.code_status,
            )
        except Exception as ex:
            return self.error_response(
                message="Error al eliminar el usuario", error=str(ex)
            )
