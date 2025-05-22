from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schema.questions_schema import Question
from repository.questions_repo import get_questions, get_question_selected_by_id, exclude_question, edit_question, new_question, get_question_filtered


router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}}
)

# Implement pagination, status code/standart response, users route to admin users, validation

@router.get("/")
async def questions_list():
    # Controller
    result = get_questions()
    for r in result:
        r.check_type()
    # ---
    result = jsonable_encoder(result)
    return JSONResponse(
        content={"data": result}, 
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

@router.get("/{question_column}/{column_info}")
async def get_question_selected_by_column(question_column: str, column_info: str):
    question_filtered = get_question_filtered(question_column, column_info)
    question_filtered = jsonable_encoder(question_filtered)
    return JSONResponse(
        content={"data": question_filtered},
        status_code=status.HTTP_200_OK
    )

@router.delete("/{question_id}")
async def delete_question_by_id(question_id):
    exclude_question(question_id)
    return {"question deleted"}

@router.put("/{question_id}")
async def edit_question_by_id(question: Question):
    edit_question(question)
    return {"question edited"}

@router.post("/")
async def create_question(question: Question):
    new_question(question.type, question.subject, question.topic, question.statement, 
                question.answer_to_print, question.correct_answer)
    return {"Message": "Success"}