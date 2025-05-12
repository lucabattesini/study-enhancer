from pydantic import BaseModel

class question_schema(BaseModel):
    id: str
    type: str
    subject: str
    topic: str
    statement: str
    answer_to_print: str
    correct_answer: str