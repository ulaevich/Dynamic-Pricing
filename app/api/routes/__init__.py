from fastapi import APIRouter

from ..routes.default import router as default_router


main_router = APIRouter()
main_router.include_router(default_router)