from admin import create_question
from user import print_questions

def show_main_menu():
    print(f"MAIN MENU: ")
    print(f"1. Manage questions")
    print(f"2. Answer questions")
    return input("> ")

def show_admin_menu():
    print(f"A. Create questions")
    print(f"B. View questions")
    print(f"C. Edit questions")
    print(f"D. Delete questions")
    print(f"0. Exit")
    return input("> ")

def run_admin(sub_menu_answer):
    match sub_menu_answer.lower():
        case "a":
            return create_question()
        case "b":
            return print("B")
        case "c":
            return print("C")
        case "d":
            return print("D")
        case "0":
            return

def menu_controler(): 
    answer = "1000"
    while answer != "0":
        answer = show_main_menu()
        if answer == "1":
            sub_menu_answer = show_admin_menu()
            run_admin(sub_menu_answer)
        elif answer == "2":
            print_questions()