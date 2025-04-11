import sqlite3

# Make a connection with the db
connection = sqlite3.connect("./db/questions.db")

# Create a cursor to execute the SQL commands
cursor = connection.cursor()

# Create a table
def create_a_table(table_name, first_component, second_component, 
                   third_component, fourth_component, fifth_component) :
    cursor.execute(f'''
    CREATE A TABLE IF NOT EXISTS {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    {first_component} TEXT NOT NULL,
    {second_component} TEXT NOT NULL,
    {third_component} TEXT NOT NULL,
    {fourth_component} TEXT NOT NULL,
    {fifth_component} TEXT NOT NULL
    )''')
    # Save the changes
    connection.commit()
    # Close the connection with the db
    connection.close()