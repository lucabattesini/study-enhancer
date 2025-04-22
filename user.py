from db.questions import get_questions

def print_questions() :
    questions = get_questions()
    for q in questions:
        print(q['statement'])
        answer = input("True or False? > ")
        if answer == q['correct_answer']:
            print("You're right!")
        else:
            print("You're wrong!")
        print("===" * 10)