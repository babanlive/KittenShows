from core.config import settings
from fastapi import APIRouter

from .breeds import router as breeds_router
from .kittens import router as kittens_router


router = APIRouter(prefix=settings.api.v1.prefix,)

router.include_router(router=breeds_router, prefix=settings.api.v1.breeds,)
router.include_router(router=kittens_router, prefix=settings.api.v1.kittens,)
