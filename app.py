from fastapi import FastAPI

from routers import questions, profiles

app = FastAPI()

app.include_router(questions.router)
app.include_router(profiles.router)

@app.get("/")
async def root():
    return{"message": "Main route"}
