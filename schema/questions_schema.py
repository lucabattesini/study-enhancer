from pydantic import BaseModel

class Question(BaseModel):
    type: str | None
    subject: str | None
    topic: str | None
    statement: str
    answer_to_print: str| None
    correct_answer: str

    # If question type = multiple_questions and answer to print = none . Error