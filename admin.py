from db.questions import new_question, get_questions

# The next functions will work as a CRUD

# Create a new question in questions table
def create_question() :
    print("Inserting a new question")
    print("===" * 6)
    print("Fill out the following:")
    question = str(input("Write the question statement > "))
    answer = str(input("True/False? > "))
    new_question(question, answer)

# Will show all the db questions
def show_questions() :
    print("Questions list:")
    print("===" * 6)
    questions = get_questions()
    for index, q in enumerate(questions):
        print(f"{index+1}. {q['statement']}")
        print(f"Answer: {q['correct_answer']}")
        print(f"Subject: {q['subject']}")
        print(f"Type: {q['type']}")
        print(f"Topic: {q['topic']}")
        print(f"Answer to Print: {q['answer_to_print']}")
        print(f"---")
