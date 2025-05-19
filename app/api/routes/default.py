from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.settings import SETTINGS
from pydantic import BaseModel
from typing import Literal
from pathlib import Path
from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/")
async def root():
    return JSONResponse(status_code=200, content={"message": "DYNAMIC-PRICING"})
