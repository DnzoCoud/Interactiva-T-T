from pydantic import BaseModel, Field
from typing import Optional


class UserPatchDto(BaseModel):
    cedula: Optional[str] = None
    username: Optional[str] = None


class UserCreateDto(BaseModel):
    cedula: str = Field(..., max_length=20)
    username: str = Field(..., max_length=20)


class UserResponseDto(BaseModel):
    id: int
    cedula: str
    username: str
