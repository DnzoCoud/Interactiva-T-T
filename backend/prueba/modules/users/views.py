from rest_framework.views import APIView
from pydantic import ValidationError as PydanticValidationError
from modules.users.dtos import UserCreateDto
from rest_framework.response import Response
from rest_framework import status
from modules.users.serializers import UserSerializer
from modules.users.services import UserService
from modules.common.views import BaseAPIView


# Create your views here.
class UserCreateView(BaseAPIView):
    def post(self, request):
        try:
            dto_data = UserCreateDto(**request.data)
        except PydanticValidationError as e:
            return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

        new_user_dto = UserService.create_user(dto_data)
        serializer = UserSerializer(data=new_user_dto.model_dump())
        if serializer.is_valid():
            return self.success_response(data=serializer.data)
        return self.error_response(
            message="Hubo un error al obtener los usuarios", error=str(e)
        )


class UserListView(BaseAPIView):
    def get(self, request):
        users = UserService.get_all()
        serializer = UserSerializer(users, many=True)
        return self.success_response(data={"users": serializer.data})
