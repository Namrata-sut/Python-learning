from fastapi import APIRouter, Depends, Form, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import RedirectResponse

from app.db.db_connection import get_db
from app.schemas.user_schema import CreateUserRequest, UserResponse
from app.services.user_service import UserService
from app.utils import hash_pass

signup_login_router = APIRouter()

signup_login_router.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@signup_login_router.get("/signup")
async def signup(request: Request):
    """
    Render the signup page.
    Args:
        request (Request): The FastAPI request object.
    Returns:
        TemplateResponse: Renders the `index.html` template with the signup page.
    """
    return templates.TemplateResponse("index.html", {"request": request, "page": "signup"})


@signup_login_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
        name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        db: AsyncSession = Depends(get_db)
):
    """
        handle user signup by creating a new user in the database.
        Args:
            name (str): The user's name (from form data).
            email (str): The user's email (from form data).
            password (str): The user's password (from form data, hashed before storing).
            db (AsyncSession): Database session dependency.
        Returns:
            RedirectResponse: Redirects to the login page after successful registration.
        """
    try:
        hashed_pass = hash_pass(password)
        user = CreateUserRequest(
            username=name,
            email=email,
            password=hashed_pass
        )
        await UserService.add_user(user, db)
        return RedirectResponse(url="/login", status_code=303)
    except Exception as e:
        return {"Error Occurred": e}


@signup_login_router.get("/login")
async def login(request: Request):
    """
        Render the login page.
        Args:
            request (Request): The FastAPI request object.
        Returns:
            TemplateResponse: Renders the `index.html` template with the login page.
        """
    return templates.TemplateResponse("index.html", {"request": request, "page": "login"})


@signup_login_router.post("/login")
async def login(user_details: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    """
       authenticate the user and generate an access token.
       Args:
           user_details (OAuth2PasswordRequestForm): The user's login credentials (username and password).
           db (AsyncSession): Database session dependency.
       Returns:
           RedirectResponse: Redirects to `/get_all_quizzes` upon successful login.
                            store the access token in a secure HTTP-only cookie.
    """
    try:
        access_token = await UserService.get_user(user_details, db)
        response = RedirectResponse(url="/get_all_quizzes", status_code=303)
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response
    except Exception as e:
        return {"Error Occurred": e}


@signup_login_router.post("/logout")
async def logout(request: Request, response: Response):
    """
    log out the user by deleting the access token cookie.
    Args:
        request (Request): The FastAPI request object (to access cookies).
        response (Response): The FastAPI response object (to delete cookies).
    Returns:
        dict: A message confirming successful logout.
    """
    try:
        token = request.cookies.get("access_token")
        if token:
            response.delete_cookie("access_token")

        return {"message": "Logged out successfully"}
    except Exception as e:
        return {"Error Occurred": e}
