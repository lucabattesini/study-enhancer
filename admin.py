from db.questions import new_question

def create_question() :
    print("Inserting a new question")
    print("===" * 6)
    print("Fill out the following:")
    question = str(input("Write the question statement > "))
    answer = str(input("True/False? > "))
    new_question(question, answer)