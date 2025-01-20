from pydantic import BaseModel, Field


class UserCreateDto(BaseModel):
    cedula: str = Field(..., max_length=20)
    username: str = Field(..., max_length=20)


class UserResponseDto(BaseModel):
    id: int
    cedula: str
    username: str
