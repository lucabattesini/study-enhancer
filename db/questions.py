from db.connection import cursor, connection
from uuid import uuid1

def new_question(question, answer, answer_to_print, question_type, question_subject, question_topic) :
    '''
    Will insert a new id, question and answer to the questions table
    '''
    id = uuid1()
    cursor.execute(f"INSERT INTO questions (id, type, statement, answers_to_print, correct_answer, subject, topic) VALUES ('{id}', '{question_type}', '{question}', '{answer_to_print}', '{answer}', '{question_subject}', '{question_topic}')")
    connection.commit()

def exclude_question(id) :
    '''
    Delete a question in the db
    '''
    cursor.execute(f"DELETE FROM questions WHERE id = '{id}'")
    connection.commit()

def edit_question(id, object_to_change, change) :
    cursor.execute(f"UPDATE questions SET {object_to_change} = '{change}' WHERE id = '{id}'")
    connection.commit()

def parse_question(params) :
    '''
    Will organize the vars of the table in an object
    '''
    return {
        'id': params[0],
        'type': params[1],
        'subject': params[2],
        'topic': params[3],
        'statement': params[4],
        'answer_to_print': params[5],
        'correct_answer': params[6]
    }

def get_questions() :
    '''
    Will get the questions from the db, an will organize with parse_question()
    ''' 
    res = cursor.execute(f"SELECT * FROM questions")
    list_result = res.fetchall()
    list_objects = []
    for r in list_result:
        list_objects.append(parse_question(r))
    return list_objects
    
def get_question_selected_by_id(question_id) :
    '''
    Will get the questions from the db, an will organize with parse_question()
    ''' 
    list = get_questions()
    for r in list:
        if question_id == r["id"]:
            return r
    