import json
from optparse import Option
from os import system, name
import sys

def main():
    clear()
    greet_user()
    option = show_menu()
    print(option)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def greet_user():
    # Greet user and display menu
    print("Welcome to Flashy!\n")

def show_menu():
    print("1. Review flashcards")
    print("2. Create flashcards")
    print("3. Delete flashcards")
    
    option = 0
    while option not in ("1", "2", "3"):
        option = input("Please enter an option number: ")
    return(option)
            



if __name__ == '__main__':
    sys.exit(main()) 






