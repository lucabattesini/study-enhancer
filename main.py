from fastapi import FastAPI
from menus import menu_controler
from db.questions import get_questions

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/questions")
async def questions_list():
    return get_questions() 

@app.get("/questions/{question_id}")
async def read_question(question_id):
    return {"question_id": question_id}

# to do