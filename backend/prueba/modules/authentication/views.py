from modules.common.views import BaseAPIView
from rest_framework.permissions import AllowAny
from modules.authentication.serializers import AuthTokenSerializer
from rest_framework.exceptions import ValidationError
from modules.authentication.services import AuthService
from modules.common.exceptions import UnauthorizeException


class AuthTokenView(BaseAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer)
            acces_token, refresh_token = AuthService.authenticate_user(
                serializer.validated_data["cedula"],
                serializer.validated_data["password"],
            )
            return self.success_response(
                data={
                    "access": acces_token,
                    "refresh": refresh_token,
                }
            )
        except UnauthorizeException as ue:
            return self.error_response(
                status_code=ue.code_status,
                message=str(ue.message),
                error=str(ue.message),
            )
        except Exception as ex:
            return self.error_response(
                message=str(ex),
                error=str(ex),
            )
