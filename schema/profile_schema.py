from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    permission: str
    questions_answered: int
    correct_questions: int