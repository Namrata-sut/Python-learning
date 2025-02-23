import enum
from typing import Optional
from pydantic import BaseModel

from app.models.user_model import UserRole


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str


class DataToken(BaseModel):
    id: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: UserRole
