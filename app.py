from fastapi import FastAPI

from routers import questions

app = FastAPI()

app.include_router(questions.router)

@app.get("/")
async def root():
    return{"message": "Hello World!"}