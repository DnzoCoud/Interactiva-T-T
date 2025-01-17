from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, cedula, password=None, **extra_fields):
        if not cedula:
            raise ValueError("El usuario debe tener una cédula")
        user = self.model(cedula=cedula, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    cedula = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True, default=None)
    objects = CustomUserManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.cedula
