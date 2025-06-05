from pydantic import BaseModel

class Question(BaseModel):
    id: str
    type: str | None
    subject: str | None
    topic: str | None
    statement: str
    answers_to_print: str| None
    correct_answer: str

    @classmethod
    def check_type(cls):
        if type and type == 'true_or_false':
            print("1")