from db.questions import get_questions
from utils import clean_terminal

def print_questions(question_type) :
    '''
    Show all the questions, ask for an answer
    and give a feedback if you're right or wrong
    '''
    questions = get_questions()
    correct = int(0)
    wrong = int(0)
    question_number = int(0)
    question_subject = str(input("What's the subject you want to answer?"))
    question_topic = str(input("What's the question topic you want to answer?"))
    for q in questions:
        clean_terminal()
        if question_type == q['type']:
            if question_subject == q['subject']:
                if question_topic == q['topic']:
                    question_number = question_number + 1
                    print(f"QUESTION {question_number}")
                    print(q['statement'])
                    print("=" * 10)
                    answer = input(q['answer_to_print'])
                    if answer == q['correct_answer']:
                        correct = correct + 1
                    else:
                        wrong = wrong + 1
                else:
                    print("We don't have this question topic in our data base, please try again later")
    
    clean_terminal()
    print("=" * 10)
    hit_percentage = correct / question_number * 100
    print(f"You did {correct} correct and {wrong} wrong")
    input(f"It means you're {hit_percentage}% correct > ")