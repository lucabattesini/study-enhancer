from db.questions import new_question, get_questions

def menu():
    print(f"MENU: ")
    print(f"1. Insert a new question")
    print(f"2. Answer questions")
    return input("> ")

def insert_question() :
    print("Inserting a new question")
    print("===" * 6)
    print("Fill out the following:")
    question = str(input("Write the question statement > "))
    answer = str(input("True/False? > "))
    new_question(question, answer)

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

def main(): 
    print(f"Welcome \n ")
    answer = "4"
    while answer != "0":
        answer = menu()
        if answer == "1":
            insert_question()
        elif answer == "2":
            print_questions()




main()
