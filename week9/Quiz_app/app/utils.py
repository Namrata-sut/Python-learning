from datetime import datetime, timedelta, UTC
from fastapi import Depends, HTTPException, status
from fastapi import Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_connection import get_db
from app.models.user_model import User, UserRole
from app.schemas.user_schema import DataToken

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# takes plain text password input and returns a hashed version of it and securely stored in the database.
def hash_pass(password: str):
    """
    Hashes a plaintext password using bcrypt.
    Args:
        password (str): The plaintext password.
    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def verify_password(non_hashed_pass, hashed_pass):
    """
     Verifies if a given plaintext password matches the stored hashed password.
     Args:
         non_hashed_pass (str): The plaintext password.
         hashed_pass (str): The hashed password.
     Returns:
         bool: True if the passwords match, False otherwise.
     """
    return pwd_context.verify(non_hashed_pass, hashed_pass)


def create_access_token(data: dict):
    """
    Generates a JWT access token with an expiration time.
    Args:
        data (dict): The data to encode in the token.
    Returns:
        str: Encoded JWT access token.
    """
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": int(expire.timestamp())})
    encoded_jwt = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_token_access(token: str, credentials_exception):
    """
        Decodes and verifies a JWT access token.
        Args:
            token (str): The JWT token.
            credentials_exception (HTTPException): Exception to raise if token verification fails.
        Returns:
            DataToken: The extracted token data.
        Raises:
            HTTPException: If the token is invalid or expired.
        """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # `exp` is automatically checked here
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = DataToken(id=str(id))
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise credentials_exception
    return token_data


async def get_current_user(request: Request, db: AsyncSession = Depends(get_db)):
    """
        retrieves the current authenticated user based on the access token.
        Args:
            request: The HTTP request object.
            db (AsyncSession): The database session.
        Returns:
            User: The authenticated user object.
        Raises:
            HTTPException: If the token is missing, invalid, or the user does not exist.
    """
    access_token: str = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="Missing token")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Credentials.."
    )
    token_data = verify_token_access(access_token, credentials_exception)
    user_id = getattr(token_data, "id", None)
    user = await db.execute(select(User).where(User.id == int(user_id)))
    user = user.scalars().first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


async def admin_only(user_data=Depends(get_current_user)):
    """
    Ensures that the user has admin privileges.
    Args:
        user_data (User): The authenticated user.
    Returns:
        User: The admin user.
    Raises:
        HTTPException: If the user is not an admin.
    """
    if user_data.role != UserRole.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: Admins only")
    return user_data
