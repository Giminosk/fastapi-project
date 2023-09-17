from fastapi import APIRouter

from .users.router import router as router_users
from .profiles.router import router as router_profiles


api_router = APIRouter()


api_router.include_router(
    router=router_users,
    prefix="/users",
)


api_router.include_router(
    router=router_profiles,
    prefix="/profiles",
)
