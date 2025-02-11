from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.routes.question import question_router
from app.routes.quiz import quiz_router
from app.routes.score_count import score_router

app = FastAPI()

app.include_router(router=question_router)
app.include_router(router=quiz_router)
app.include_router(router=score_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello gamers!"})
