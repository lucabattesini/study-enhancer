from db.connection import cursor, connection
from uuid import uuid1

def new_question(question, answer) :
    id = uuid1()
    cursor.execute(f"INSERT INTO questions (id, statement, correct_answer) VALUES ('{id}', '{question}', '{answer}')")
    connection.commit()