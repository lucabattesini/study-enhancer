from db.connection import cursor, connection
from uuid import uuid1
from schema.profile_schema import Profile

def parse_profiles(params) -> Profile:
    '''
    Will organize the vars of the table in an object
    '''
    return Profile(
        name=params[0],
        permission=params[1],
        questions_answered=params[2],
        correct_questions=params[3]
    )
def create_profile(name, permission, questions_answered, correct_questions):
    '''
    Will create a new profile
    '''
    id = str(uuid1())
    cursor.execute("INSERT INTO profiles (id, name, permission, questions_answered, correct_questions) VALUES (?, ?, ?, ?, ?)",
                   (id, name, permission, questions_answered, correct_questions))
    connection.commit()

def get_profiles():
    '''
    Will get the profiles from the db, an will organize with parse_question()
    ''' 
    res = cursor.execute(f"SELECT * FROM profiles")
    list_result = res.fetchall()
    list_objects = []
    for r in list_result:
        list_objects.append(parse_profiles(r))
    return list_objects

def exclude_profile(id):
    '''
    Delete a profile
    '''
    cursor.execute(f"DELETE FROM profiles WHERE id = '{id}'")
    connection.commit()

def edit_profile(id, object_to_change, change):
    """
    Edit an specific profile
    """
    cursor.execute(f"UPDATE profiles SET {object_to_change} = '{change}' WHERE id = '{id}'")
    connection.commit()