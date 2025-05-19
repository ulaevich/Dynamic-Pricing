import logging
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.routes import main_router


from app.settings import SETTINGS


app = FastAPI()
# app.add_middleware(BaseHTTPMiddleware, dispatch=)
app.include_router(main_router)


@app.on_event("startup")
async def app_startup():

    pass
