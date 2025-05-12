from fastapi import FastAPI
from schemas import Question
from db.questions import get_questions, get_question_selected_by_id, exclude_question, edit_question, new_question

app = FastAPI()

@app.get("/questions")
async def questions_list():
    """Return all questions"""
    return get_questions() 

@app.get("/questions/{question_id}")
async def get_question_by_id(question_id):
    """
    Return 1 question
    /questions/{question_id}
    """
    return get_question_selected_by_id(question_id)

@app.delete("/questions/{question_id}")
async def delete_question_by_id(question_id):
    """
    Delete 1 question
    @app.delete("/questions/{question_id}")
    """
    exclude_question(question_id)
    return {"question deleted"}

@app.put("/questions/{object_to_change}/{change}/{question_id}")
async def edit_question_by_id(object_to_change, change, question_id):
    """PUT
    @app.put("/questions/{question_id}")
    usar body ao invés de params
    receber o objeto inteiro com as alterações
    fazer validações
    """
    edit_question(question_id, object_to_change, change)
    return {"question edited"}

@app.post("/questions")
async def create_question(question: Question):
    new_question(question.type, question.subject, question.topic, question.statement, 
                question.answer_to_print, question.correct_answer)
    return {"question created"}