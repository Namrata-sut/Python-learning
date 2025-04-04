from fastapi import FastAPI

from app.routes.expense import router

app = FastAPI()

app.include_router(router=router)
