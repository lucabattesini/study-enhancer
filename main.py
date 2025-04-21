from db.connection import cursor

def menu():
    print(f"MENU: ")
    print(f"1. Insert a new question")
    print(f"2. Answer questions")
    return input("> ")

def main(): 
    print(f"Welcome \n ")
    answer = menu()
    if answer == "1":
        print("Create a new question")
    elif answer == "2":
        print("Answer a question")

main()