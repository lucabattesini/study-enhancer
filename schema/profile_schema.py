from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    permission: str
    questions_answered: int | None
    correct_questions: int | None