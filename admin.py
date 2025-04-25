from db.questions import new_question, get_questions, exclude_question
from utils import clean_terminal, select_object_to_edit

# The next functions will work as a CRUD

def create_question() :
    '''
    Create a new question in questions table
    '''
    print("INSERTING A NEW QUESTION")
    print("===" * 10)
    print("Fill out the following")
    print("===" * 10)
    question_type = str(input("Question type (true_false or multiple_choices) > "))
    question = str(input("Write the question statement > "))
    answer_to_print = str(input("Answer to show to the user > "))
    answer = str(input("Correct answer > "))
    new_question(question, answer, answer_to_print, question_type)

def delete_question() :
    '''
    Create an interface showing the questions and 
    asking wich one you want to delete
    '''
    questions = show_questions(stop_view=False)
    position = int(input(f"Select question number to delete >"))
    if len(questions) >= position > 0:
        question_to_delete = questions[position-1]
        exclude_question(question_to_delete['id'])
    else:
        print("===" * 10)
        print("Undefined question number")
        print("===" * 10)
        delete_question()

def select_question_to_edit() :
    questions = show_questions(stop_view=False)
    position = int(input(f"Select question number to edit > "))
    if len(questions) >= position > 0:
        question_to_edit = questions[position-1]
        select_object_to_edit(question_to_edit['id'])
    else:
        print("===" * 10)
        print("Undefined question number")
        print("===" * 10)
        select_question_to_edit()
        
def show_questions(stop_view=True) :
    '''
    Will show all the db questions
    '''
    clean_terminal()
    print("QUESTION LIST")
    print("===" * 10)
    questions = get_questions()
    for index, q in enumerate(questions):
        print(f"{index+1}. {q['statement']}")
        print(f"Answer: {q['correct_answer']}")
        print(f"Subject: {q['subject']}")
        print(f"Type: {q['type']}")
        print(f"Topic: {q['topic']}")
        print(f"Answer to Print: {q['answer_to_print']}")
        print("===" * 10)
        print("===" * 10)
    if stop_view:
        input("Press any key to go to main menu > ") 
    return questions
    
