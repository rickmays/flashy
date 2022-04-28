import json
from optparse import Option
from os import system, name
import sys

flashcards = {}

def main():
    flashcards = read_flashcards_from_disk()

    clear()
    print(flashcards)
    greet_user()
    show_menu()
    option = get_option()
    process_menu_option(option)

def read_flashcards_from_disk():
    with open('flashcards.json') as json_file:
        flashcards = json.load(json_file)
        return flashcards

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
    
def get_option():
    option = 0
    while option not in ("1", "2", "3"):
        option = input("Please enter an option number (1-3): ")
    return(option)

def process_menu_option(option):
    if option == str(1):
        print("Review Flashcards")
    elif option == str(2):
        create_flashcard()
    elif option == str(3):
        print("Delete Flashcard")
    

def create_flashcard():
    while(True):
        front = input("Please enter text for flashcard front (word, question, etc.: ")
        back = input("Please enter text for flashcard back (definition, answer, etc.: ")
        flashcards[front] = back
        print(flashcards)
        with open('flashcards.json', 'w') as outfile:
            json.dump(flashcards, outfile)
        front = ""
        back = ""


if __name__ == '__main__':
    sys.exit(main()) 






