from uuid import uuid4

from fastapi import FastAPI, Request, Form, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import RedirectResponse

from app.utils import hash_pass, verify_password, create_access_token
from app.db.db_connection import get_db
from app.models.user_model import User
from app.schemas.user import CreateUserRequest, UserResponse
# from app.utils import get_hashed_password, verify_password, create_access_token, create_refresh_token

signup_login_router = APIRouter()

signup_login_router.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@signup_login_router.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "signup"})


@signup_login_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_users(name: str = Form(...), email: str = Form(...), password: str = Form(...),
                 db: AsyncSession = Depends(get_db)):

    hashed_pass = hash_pass(password)
    user = CreateUserRequest(
        username=name,
        email=email,
        password=hashed_pass
    )

    new_user = User(username=user.username,
                    email=user.email,
                    password=user.password,
                    role=user.role)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return RedirectResponse(url="/login", status_code=303)


@signup_login_router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "login"})


@signup_login_router.post("/login")
async def login(user_details: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user_details.username))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=401, detail="The User does not exist")

    if not verify_password(user_details.password, user.password):
        raise HTTPException(status_code=401, detail="The Passwords do not match")

    access_token = create_access_token(data={"user_id": user.id})

    response = RedirectResponse(url="/get_all_quizzes", status_code=303)
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return response
