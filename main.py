from db.questions import new_question

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

def main(): 
    print(f"Welcome \n ")
    answer = menu()
    if answer == "1":
        insert_question()
    elif answer == "2":
        print("Answer a question")



main()