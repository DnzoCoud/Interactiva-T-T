from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, cedula, username, password=None, **extra_fields):
        if not cedula:
            raise ValueError("El usuario debe tener una cédula")
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")

        user = self.model(cedula=cedula, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    cedula = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "cedula"

    def __str__(self):
        return f"{self.username} ({self.cedula})"
