from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.routes.question_route import question_router
from app.routes.quiz_route import quiz_router
from app.routes.score_count_route import score_router
from app.routes.signup_login_route import signup_login_router
from app.routes.user_route import user_router

app = FastAPI()

app.include_router(router=question_router)
app.include_router(router=quiz_router)
app.include_router(router=score_router)
app.include_router(router=signup_login_router)
app.include_router(router=user_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello gamers!"})
