from admin import create_question, show_questions, delete_question
from user import print_questions
from utils import clean_terminal

# Just show the opitions of the main menu
def show_main_menu():
    clean_terminal()
    print("========== MAIN MENU ===========")
    print("1. Manage questions")
    print("2. Answer questions")
    print("0. Exit")
    print("=" * 32)
    return input("> ")

# just show the opitions of the manager menu
def show_admin_menu():
    clean_terminal()
    print("========== MANAGER MENU ===========")
    print("A. Create questions")
    print("B. View questions")
    print("C. Edit questions")
    print("D. Delete questions")
    print("0. Back to main menu")
    print("=" * 35)
    return input("> ")

# Run a specific function for each chosen menu opition
def run_admin(sub_menu_answer):
    match sub_menu_answer.lower():
        case "a":
            return create_question()
        case "b":
            return show_questions()
        case "c":
            return print("C")
        case "d":
            return delete_question()
        case "0": # Leave the manager menu and come back to the main menu
            return

# Depending of your chosen opition, will run the function of the manager menu or the user menu
def menu_controler(): 
    answer = "1000"
    while answer != "0":
        answer = show_main_menu()
        if answer == "1":
            sub_menu_answer = show_admin_menu()
            run_admin(sub_menu_answer)
        elif answer == "2":
            print_questions()