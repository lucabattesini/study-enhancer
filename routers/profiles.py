from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repository.profiles_repo import get_profiles, create_profile, exclude_profile, edit_profile
from schema.profile_schema import Profile

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

@router.post("/")
async def new_db_profile(profile: Profile):
    '''
    Create profile
    '''
    create_profile(profile.name, profile.permission, profile.questions_answered, profile.correct_questions)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Profile created successfully"}
    )

@router.put("/")
async def edit_db_profile(profile: Profile):
    '''
    Edit a profile
    '''
    edit_profile(profile.id, profile.name, profile.permission, profile.questions_answered, profile.correct_questions)
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Profile edited successfully"}
                        )

@router.delete("/{profile_id}")
async def delete_db_profile(profile_id):
    '''
    Delete a profile
    '''
    exclude_profile(profile_id)
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Profile deleted successfully"}
                        )