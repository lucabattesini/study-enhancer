import os
from db.questions import edit_question

def clean_terminal() :
    """
    Clean the last things wrote in the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def select_object_to_edit(id) :
    object_to_change = input("Type the object in the question you want to edit > ")
    change = input("Type the change you want to do > ")
    edit_question(id, object_to_change, change)