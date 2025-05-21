from pydantic import BaseModel

class Question(BaseModel):
    type: str | None
    subject: str | None
    topic: str | None
    statement: str
    answer_to_print: str| None
    correct_answer: str

    # If question type = multiple_questions and answer to print = none . Error

    @classmethod
    def check_type(cls):
        if type and type == 'true_or_false':
            print("1")