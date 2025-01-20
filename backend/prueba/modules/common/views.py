from rest_framework.views import APIView
from rest_framework.response import Response


class BaseAPIView(APIView):
    def success_response(
        self, status_code=200, data=None, message="Operación realizada con exito"
    ):
        return Response(
            {
                "status": "success",
                "code": status_code,
                "data": data if data is not None else None,
                "message": message,
            },
            status=status_code,
        )

    def error_response(
        self, status_code=500, message="Hubo un error en la operación", error=None
    ):
        response = {
            "status": "error",
            "code": status_code,
            "data": None,
            "message": message,
        }
        if error:
            response["error"] = error
        return Response(response, status=status_code)
