from fastapi import APIRouter

from ..routes.default import router as default_router
from ..routes.pridict import router as predict_router


main_router = APIRouter()
main_router.include_router(default_router)
main_router.include_router(predict_router)
