from fastapi import APIRouter
from schema.questions_schema import Question
from repository.questions_repo import get_questions, get_question_selected_by_id, exclude_question, edit_question, new_question


router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}}
)

@router.get("/") # Implement filters, implement pagination, status code/standart response,users route to admin users, validation, 
async def questions_list():
    result = get_questions() 
    print(result)
    for r in result:
        r.check_type()
    return result

@router.get("/{question_id}")
async def get_question_by_id(question_id):
    return get_question_selected_by_id(question_id)

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
    return {"question created"}