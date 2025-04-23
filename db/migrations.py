from connection import cursor

# Create a table
cursor.execute("CREATE TABLE questions(id, type, subject, topic, statement, answers_to_print , correct_answer)")