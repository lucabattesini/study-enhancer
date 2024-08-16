def true_or_false(question, result) :
    print(f"{question}")
    answer = str("Write 'T' for true or 'F' for false")
    if answer == "f" or "F" :
        if result == False:
            print("Congratulations, right answer")
        else:
            print("Wrong answer")
    elif answer == "t" or "T" :
        if result == True:
            print("Congratulations, right answer")
        else:
            print("Wrong answer")