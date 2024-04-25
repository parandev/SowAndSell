from fastapi import APIRouter

from api.api_v1.endpoints import farmer

api_router = APIRouter()
api_router.include_router(farmer.router, prefix='/farmers', tags=['farmers'])