from fastapi import Cookie
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User, UserRole
from app.schemas.user_schema import DataToken

from datetime import timedelta, datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.db.db_connection import get_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# takes plain text password input and returns a hashed version of it and securely stored in the database.
def hash_pass(password: str):
    return pwd_context.hash(password)

def verify_password(non_hashed_pass, hashed_pass):
    return pwd_context.verify(non_hashed_pass, hashed_pass)


def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})
    encoded_jwt = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_token_access(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = DataToken(id=str(id))
    except JWTError as e:
        print(e)
        raise credentials_exception
    return token_data


async def get_current_user(access_token: str = Cookie(None), db: AsyncSession = Depends(get_db)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Missing token")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    token_data = verify_token_access(access_token, credentials_exception)
    user_id = getattr(token_data, "id", None)
    user = await db.execute(select(User).where(User.id == int(user_id)))
    user = user.scalars().first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


async def admin_only(user_data=Depends(get_current_user)):
    if user_data.role != UserRole.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied: Admins only")
    return user_data
