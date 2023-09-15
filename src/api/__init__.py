from fastapi import APIRouter

from .users.router import router as router_users


api_router = APIRouter()

api_router.include_router(
    router=router_users,
    prefix="/users",
)
