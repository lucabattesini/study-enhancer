from fastapi import FastAPI
from schema.questions_schema import Question
from repository.questions_repo import get_questions, get_question_selected_by_id, exclude_question, edit_question, new_question

app = FastAPI()

@app.get("/questions")
async def questions_list():
    result = get_questions() 
    print(result)
    for r in result:
        r.check_type()
    return result

@app.get("/questions/{question_id}")
async def get_question_by_id(question_id):
    return get_question_selected_by_id(question_id)

@app.delete("/questions/{question_id}")
async def delete_question_by_id(question_id):
    exclude_question(question_id)
    return {"question deleted"}

@app.put("/questions/{question_id}")
async def edit_question_by_id(question: Question):
    edit_question(question)
    return {"question edited"}

@app.post("/questions")
async def create_question(question: Question):
    new_question(question.type, question.subject, question.topic, question.statement, 
                question.answer_to_print, question.correct_answer)
    return {"question created"}