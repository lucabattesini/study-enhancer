from admin import create_question, show_questions, delete_question, select_question_to_edit
from user import print_questions
from utils import clean_terminal

def show_main_menu():
    '''
    Just show the opitions of the main menu
    '''
    clean_terminal()
    print("========== MAIN MENU ===========")
    print("1. Manage questions")
    print("2. Answer questions")
    print("0. Exit")
    print("=" * 32)
    return input("> ")

def show_admin_menu():
    '''
    Just show the opitions of the manager menu
    '''
    clean_terminal()
    print("==== MANAGER MENU ====")
    print("A. Create questions")
    print("B. View questions")
    print("C. Edit questions")
    print("D. Delete questions")
    print("0. Back to main menu")
    print("=" * 35)
    return input("> ")

def show_user_menu() :
    print("===== USER MENU =====")
    print("What type of question you want to answer?")
    print("A. True or False \nB. Multiple choices")
    question_type = input("> ")
    if question_type == "a":
        print_questions("true_or_false")
    elif question_type == "b":
        print_questions("multiple_answer")

def run_admin(sub_menu_answer):
    '''
    Run a specific function for each chosen menu opition
    '''
    match sub_menu_answer.lower():
        case "a":
            return create_question()
        case "b":
            return show_questions()
        case "c":
            return select_question_to_edit()
        case "d":
            return delete_question()
        case "0": # Leave the manager menu and come back to the main menu
            return

def menu_controler():
    '''
    Depending of your chosen opition, 
    will run the function of the manager menu or the user menu
    '''
    answer = "1000"
    while answer != "0":
        answer = show_main_menu()
        if answer == "1":
            sub_menu_answer = show_admin_menu()
            run_admin(sub_menu_answer)
        elif answer == "2":
            show_user_menu()