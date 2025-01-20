from rest_framework.views import APIView
from pydantic import ValidationError as PydanticValidationError
from modules.users.dtos import UserCreateDto
from rest_framework.response import Response
from rest_framework import status
from modules.users.serializers import UserSerializer
from modules.users.services import UserService


# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        try:
            dto_data = UserCreateDto(**request.data)
        except PydanticValidationError as e:
            return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

        new_user_dto = UserService.create_user(dto_data)
        serializer = UserSerializer(data=new_user_dto.model_dump())
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
