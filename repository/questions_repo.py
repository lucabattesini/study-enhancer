from db.connection import cursor, connection
from uuid import uuid1
from schema.questions_schema import Question

def new_question(question_type, question_subject, question_topic, question, answer_to_print, answer):
    '''
    Will insert a new question to the question table
    '''
    id = uuid1()
    cursor.execute(f"INSERT INTO questions (id, type, statement, answers_to_print, correct_answer, subject, topic) VALUES ('{id}', '{question_type}', '{question}', '{answer_to_print}', '{answer}', '{question_subject}', '{question_topic}')")
    connection.commit()

def exclude_question(id):
    '''
    Delete a question in the db
    '''
    cursor.execute(f"DELETE FROM questions WHERE id = '{id}'")
    connection.commit()

def edit_question(id, object_to_change, change):
    """
    Will edit an specific question base 
    """
    cursor.execute(f"UPDATE questions SET {object_to_change} = '{change}' WHERE id = '{id}'")
    connection.commit()

def parse_question(params) -> Question:
    '''
    Will organize the vars of the table in an object
    '''
    return Question(
        id=params[0],
        type=params[1],
        subject=params[2],
        topic=params[3],
        statement=params[4],
        answer_to_print=params[5],
        correct_answer=params[6]
    )

def get_questions():
    '''
    Will get the questions from the db, an will organize with parse_question()
    ''' 
    res = cursor.execute(f"SELECT * FROM questions")
    list_result = res.fetchall()
    list_objects = []
    for r in list_result:
        list_objects.append(parse_question(r))
    return list_objects
    
def get_question_selected_by_id(question_id):
    '''
    Will get the questions from the db, an will organize with parse_question()
    ''' 
    list = get_questions()
    selected_question = []
    for r in list:
        if question_id == getattr(r, "id"):
            selected_question.append(r)
    if selected_question:
        return selected_question
    else:
        return {"No itens found"}
    
def get_question_filtered(question_column, column_info):
    '''
    Will get question filtered by an specific information in an specific column
    '''
    list = get_questions()
    selected_questions = []
    for r in list:
        if column_info == getattr(r, question_column):
            selected_questions.append(r)
    if selected_questions:
        return selected_questions
    else:
        return {"No itens found"}