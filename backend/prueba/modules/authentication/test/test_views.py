from rest_framework import status
from rest_framework.test import APIClient
from modules.users.services import UserService
from modules.users.dtos import UserCreateDto
import pytest


@pytest.mark.django_db
class TestAuthToken:
    @pytest.fixture
    def create_user(self):
        """Fixture para crear un usuario con cédula y contraseña."""
        data = UserCreateDto(cedula="10203040", username="Prueba Testing")
        user = UserService.create_user(data)
        return user

    def test_authenticate_user(self, create_user):
        """Prueba para autenticar al usuario con la cédula y la contraseña."""
        client = APIClient()
        data = {"cedula": "10203040", "password": "10203040"}
        response = client.post("/api/v1/auth/login", data, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["code"] == 200
        assert "access" in response.data["data"]
        assert "refresh" in response.data["data"]
