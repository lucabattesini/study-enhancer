from fastapi import APIRouter
from repository.profiles_repo import get_profiles

router = APIRouter(
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_profiles():
    result = get_profiles()
    return result