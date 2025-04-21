import sqlite3

connection = sqlite3.connect("./db/questions.db")
cursor = connection.cursor()