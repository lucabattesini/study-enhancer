from pydantic import BaseModel

class Profile(BaseModel):
    id: str
    name: str
    permission: str
    questions_answered: int
    correct_questions: int