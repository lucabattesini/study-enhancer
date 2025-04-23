from db.questions import get_questions

# Show all the questions, ask for an answer and give a feedback if you're right or wrong
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