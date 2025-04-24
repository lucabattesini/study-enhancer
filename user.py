from db.questions import get_questions
from utils import clean_terminal

def print_questions() :
    '''
    Show all the questions, ask for an answer
    and give a feedback if you're right or wrong
    '''
    questions = get_questions()
    correct = int(0)
    wrong = int(0)
    for q in questions:
        clean_terminal()
        print(q['statement'])
        print("=" * 10)
        answer = input("True or False? > ")
        if answer == q['correct_answer']:
            correct = correct + 1
        else:
            wrong = wrong + 1
    
    clean_terminal()
    print("=" * 10)
    input(f"You did {correct} correct and {wrong} wrong")