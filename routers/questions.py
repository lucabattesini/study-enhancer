from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schema.questions_schema import Question
from repository.questions_repo import get_questions, get_question_selected_by_id, exclude_question, edit_question, new_question, get_question_filtered

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def questions_list(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1)):
    # Controller
    result = get_questions()
    paginated_result = result[skip: skip + limit]
    for r in paginated_result:
        r.check_type()
    # ---
    json_result = jsonable_encoder(paginated_result)
    return JSONResponse(
        content={"data": json_result,
                 "total": len(result),
                 "skip": skip,
                 "limit": limit
        }, 
        status_code=status.HTTP_200_OK
    )

@router.get("/{question_id}")
async def get_question_by_id(question_id):
    question = get_question_selected_by_id(question_id)
    question = jsonable_encoder(question)
    return JSONResponse(
        content={"data": question},
        status_code=status.HTTP_200_OK
    )

@router.delete("/{question_id}")
async def delete_question_by_id(question_id):
    exclude_question(question_id)
    return JSONResponse(status_code=status.HTTP_200_OK)

@router.put("/")
async def edit_question_by_id(question: Question):
    edit_question(question.id, question.type, question.subject, question.topic, question.statement, question.answers_to_print, question.correct_answer)
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Question edited successfully"}
                        )

@router.post("/")
async def create_question(question: Question):
    new_question(question.type, question.subject, question.topic, question.statement, 
                question.answer_to_print, question.correct_answer)
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Question created succesfully"})