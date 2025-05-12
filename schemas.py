from pydantic import BaseModel

class Question(BaseModel):
    type: str
    subject: str
    topic: str
    statement: str
    answer_to_print: str
    correct_answer: str