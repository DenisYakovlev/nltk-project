from fastapi import APIRouter
from schemas import PingSchema

router = APIRouter()


@router.get("/ping/", response_model=PingSchema)
async def ping():
    return {"msg": "pong"}
