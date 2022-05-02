# from curses import flash
from curses import flash
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
        create_flashcards()
        return
    elif option == str(3):
        delete_flashcards()
    elif option == str(4):
        quit()
    

def create_flashcards():
    clear()
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
    width = 72
    key_list = list(flashcards.keys())
    value_list = list(flashcards.values())
    for i in range(0, length):
        option = 'a'
        while option != "":
            clear()
            print(key_list[i], end = "\n\n")
            print("-"*width)
            print("Press enter/return key to see back of flashcard\n")
            option = input()
        clear()
        print(key_list[i], end = "\n\n")
        print(value_list[i], end = "\n\n")
        print("-"*width)
        input_string = input("Press enter/return key for next flashcard or q to return to menu: ")
        if input_string.lower() == "q":
            return
        clear()

def delete_flashcards():
    option = 'a'
    key_to_delete = -1
    clear()
    for i,j in enumerate(flashcards):
        print(f"Index: {i}, Key: {j}")
    print("\n")
    while not option.isdigit():
        option = input("Enter index to be deleted or press enter/return to exit without deleting: ")
        if option == "":
            return
    index_to_delete = int(option)
    key_list = list(flashcards.keys())
    if index_to_delete < len(key_list):
        key_to_delete = (key_list[index_to_delete])
    else:
        input("Invalid key entered, press enter/return to return to menu")
        return
    confirm_delete = input(f"DELETE Index: {index_to_delete}, Key: {key_to_delete}? (y/n) ")
    if confirm_delete.lower() != 'y':
        return
    flashcards.pop(key_to_delete, None)
    with open('flashcards.json', 'w') as outfile:
        json.dump(flashcards, outfile)
    
if __name__ == '__main__':
    sys.exit(main()) 






