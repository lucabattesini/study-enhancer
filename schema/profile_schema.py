from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    permission: str
    questions_answered: int | None
    correct_questions: int | None

class Answers(BaseModel):
    questions_answered: int
    correct_questions: int