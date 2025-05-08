from fastapi import FastAPI
from menus import menu_controler
from db.questions import get_questions, get_question_selected_by_id

app = FastAPI()

@app.get("/questions")
async def questions_list():
    return get_questions() 

@app.get("/questions/{question_id}")
async def get_question_by_id(question_id):
    return get_question_selected_by_id(question_id)