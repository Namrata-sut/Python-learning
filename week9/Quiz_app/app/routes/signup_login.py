from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

signup_login_router = APIRouter()

signup_login_router.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@signup_login_router.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "signup"})


@signup_login_router.post("/signup")
async def signup_post(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    return {"message": f"User {name} signed up successfully!"}


@signup_login_router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "login"})


@signup_login_router.post("/login")
async def login_post(request: Request, email: str = Form(...), password: str = Form(...)):
    return {"message": f"User {email} logged in successfully!"}
