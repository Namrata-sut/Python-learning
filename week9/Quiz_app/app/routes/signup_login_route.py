from fastapi import FastAPI, Request, Form, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import RedirectResponse

from app.services.user_service import UserService
from app.utils import hash_pass, oauth2_scheme
from app.db.db_connection import get_db
from app.schemas.user_schema import CreateUserRequest, UserResponse

signup_login_router = APIRouter()

signup_login_router.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@signup_login_router.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "signup"})


@signup_login_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(name: str = Form(...), email: str = Form(...), password: str = Form(...),
                 db: AsyncSession = Depends(get_db)):
    hashed_pass = hash_pass(password)
    user = CreateUserRequest(
        username=name,
        email=email,
        password=hashed_pass
    )
    new_user = await UserService.add_user(user, db)
    return RedirectResponse(url="/login", status_code=303)


@signup_login_router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "login"})


@signup_login_router.post("/login")
async def login(user_details: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    access_token = await UserService.get_user(user_details, db)
    response = RedirectResponse(url="/get_all_quizzes", status_code=303)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response
