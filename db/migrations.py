from connection import cursor

cursor.execute("CREATE TABLE questions(id, type, subject, topic, statement, answers_to_print , correct_answer)")