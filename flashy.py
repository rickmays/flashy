# from curses import flash
import json
from operator import truediv
# from optparse import Option
from os import system, name
import sys

flashcards = {}

def main():
    while(True):
        clear()
        read_flashcards_from_disk()
        greet_user()
        show_menu()
        option = get_option()
        process_menu_option(option)

def read_flashcards_from_disk():
    global flashcards
    with open('flashcards.json') as json_file:
        flashcards = json.load(json_file)

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
    print("4. Quit")
    
def get_option():
    option = 0
    while option not in ("1", "2", "3", "4"):
        option = input("Please enter an option number (1-4): ")
    return(option)

def process_menu_option(option):
    if option == str(1):
        review_flashcards()
    elif option == str(2):
        create_flashcard()
        return
    elif option == str(3):
        print("Delete Flashcard")
    elif option == str(4):
        quit()
    

def create_flashcard():
    while(True):
        print("\nWhen done entering flashcards, press enter for FRONT to exit\n")
        front = input("Please enter text for flashcard FRONT (word, question, etc.: ")
        if front == "":
            return
        back = input("Please enter text for flashcard BACK (definition, answer, etc.: ")
        flashcards[front] = back
        with open('flashcards.json', 'w') as outfile:
            json.dump(flashcards, outfile)
        clear()
        front = ""
        back = ""
        
def review_flashcards():
    length = len(flashcards)
    key_list = list(flashcards.keys())
    value_list = list(flashcards.values())
    for i in range(0, length):
        clear()
        print("Press enter/return key to see back of flashcard\n")
        print(key_list[i])
        input()
        print(value_list[i], end = "\n\n")
        input_string = input("Press enter/return key for next flashcard or q to return to menu: ")
        if input_string.lower() == "q":
            return
        clear()
        
    


if __name__ == '__main__':
    sys.exit(main()) 






