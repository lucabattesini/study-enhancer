from fastapi import FastAPI
from db.questions import get_questions, get_question_selected_by_id, exclude_question

app = FastAPI()

@app.get("/questions")
async def questions_list():
    return get_questions() 

@app.get("/questions/get/{question_id}")
async def get_question_by_id(question_id):
    return get_question_selected_by_id(question_id)

@app.get("/questions/delete/{question_id}")
async def delete_question_by_id(question_id):
    exclude_question(question_id)
    return {"question deleted"}