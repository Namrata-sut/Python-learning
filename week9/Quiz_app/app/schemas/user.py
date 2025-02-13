import enum
from typing import Optional
from pydantic import BaseModel


class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str
    role: UserRole = UserRole.user  # Default role


class DataToken(BaseModel):
    id: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: UserRole
