from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repository.profiles_repo import get_profiles

router = APIRouter(
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_profiles(skip: int= Query(0, ge=0), limit: int = Query(10, ge=1)):
    '''
    Will return all the profiles
    '''
    result = get_profiles()
    paginated_result = result[skip: skip + limit]
    json_result = jsonable_encoder(paginated_result)
    return JSONResponse(
        content={
            "data": json_result,
            "total": len(result),
            skip: skip,
            "limit": limit
        },
        status_code=status.HTTP_200_OK
    )