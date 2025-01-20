from rest_framework import status
from rest_framework.test import APIClient
from modules.users.dtos import UserCreateDto
from modules.users.services import UserService
import pytest


@pytest.mark.django_db
class TestUserView:

    @staticmethod
    @pytest.fixture
    def api_client():
        return APIClient()

    @staticmethod
    @pytest.fixture
    def create_user():
        """Fixture para crear un usuario con cédula y contraseña."""
        data = UserCreateDto(cedula="10203040", username="Prueba Testing")
        user = UserService.create_user(data)
        return user

    @staticmethod
    @pytest.fixture
    def authenticated_client(api_client, create_user):
        # Datos para autenticar al usuario
        data = {"cedula": "10203040", "password": "10203040"}
        response = api_client.post("/api/v1/auth/user/login", data)
        assert response.status_code == status.HTTP_200_OK
        access_token = response.data["data"]["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        return api_client

    def test_register_user(self, authenticated_client):
        # Datos para registrar un nuevo usuario
        data = {"cedula": "1020304050", "username": "Danielito3"}
        # Realiza la solicitud POST al endpoint de registro
        response = authenticated_client.post("/api/v1/users/", data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["data"]["user"]["username"] == "Danielito3"

    def test_get_by_id_user(self, authenticated_client, create_user):
        response = authenticated_client.get(f"/api/v1/users/{create_user.id}/")
        assert response.status_code == status.HTTP_200_OK
