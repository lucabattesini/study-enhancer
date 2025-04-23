import sqlite3

# Connect the py file with the db
connection = sqlite3.connect("./db/questions.db")
cursor = connection.cursor()