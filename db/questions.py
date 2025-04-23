from db.connection import cursor, connection
from uuid import uuid1

# Will insert a new id, question and answer to the questions table
def new_question(question, answer) :
    id = uuid1()
    cursor.execute(f"INSERT INTO questions (id, statement, correct_answer) VALUES ('{id}', '{question}', '{answer}')")
    connection.commit()

# Will organize the vars of the table in an object
def parse_question(params) :
    return {
        'id': params[0],
        'type': params[1],
        'subject': params[2],
        'topic': params[3],
        'statement': params[4],
        'answer_to_print': params[5],
        'correct_answer': params[6]
    }

# Will get the questions from the db, an will organize with parse_question()
def get_questions() : 
    res = cursor.execute(f"SELECT * FROM questions")
    list_result = res.fetchall()
    list_objects = []
    for r in list_result:
        list_objects.append(parse_question(r))
    return list_objects
    
    