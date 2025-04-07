
question = "Wrong or false"
result = True

def true_or_false(question, result) :
    print(question)
    answer = str(input("Write t for true or f for false "))
    print("=====" * 25)
    if answer == "f" :
        if result == False:
            print("Congratulations, right answer")
        if result == True:
            print("Wrong answer")
    elif answer == "t" :
        if result == True:
            print("Congratulations, right answer")
        if result == False:
            print("Wrong answer")

true_or_false(question, result)