from typing import Mapping, Any

from fastapi import APIRouter

router = APIRouter(
    # prefix="/", No prefix on root router
    tags=["root"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get() -> Mapping[str, Any]:
    return {"msg": "Hello, world"} # Returns a simple dictionary as JSON