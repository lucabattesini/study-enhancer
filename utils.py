import os

def clean_terminal() :
    """
    Clean the last things wrote in the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')