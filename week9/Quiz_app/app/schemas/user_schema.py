from typing import Optional
from pydantic import BaseModel
from app.models.user_model import UserRole


class CreateUserRequest(BaseModel):
    """
    schema for creating a new user.
    Attributes:
        username (str): The username of the new user.
        email (str): The email address of the new user.
        password (str): The password for the new user.
    """
    username: str
    email: str
    password: str


class DataToken(BaseModel):
    """
    Schema for representing a data token.
    Attributes:
        id (Optional[str]): The optional ID of the token.
    """
    id: Optional[str] = None


class UserResponse(BaseModel):
    """
    schema for user response data.
    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        role (UserRole): The role of the user (e.g., admin, user).
    """
    id: int
    username: str
    email: str
    role: UserRole


class UserUpdateSchema(BaseModel):
    """
    schema for user to update data.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        role (UserRole): The role of the user (e.g., admin, user).
    """
    username: str
    email: str
    role: UserRole


class PartialUserUpdateSchema(BaseModel):
    """
    schema for user response data.

    Attributes:
        username (str, Optional): The username of the user.
        email (str, Optional): The email address of the user.
        role (UserRole, Optional): The role of the user (e.g., admin, user).
    """
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[UserRole] = None
