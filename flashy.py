# This python project is called Flashy and it gives the user the
# ability to create, review, and delete flashcards. It stores the
# fronts and backs of the flashcards in a json file (flashcards.json) 
# and loads those into a python dictionary (flashcards) when the 
# program starts up. It was completed to fulfill the requirements of 
# the Codecademy Computer Science Pro Career Path - CS 101 course/
# section.

# Rick Mays
# Completed 5/2/2022

# The json library is needed to read and write the json file 
import json

# system and name are needed for the clear_screen() function
from os import system, name

# sys is needed for calling the main() function after all other 
# functions have been defined
import sys

# Create the empty dictionary flashcards
flashcards = {}

def main():
    # keep looping through the menu, executing the options, until the
    # user selects the quit option found in the process_menu_option
    # function
    while(True):
        clear_screen()
        read_flashcards_from_disk()
        greet_user()
        show_menu()
        option = get_option()
        process_menu_option(option)

def read_flashcards_from_disk():
    # the global keyword was required here because without that the 
    # program was interpreting it as a local variable
    global flashcards
    # open the flashcards file and load it into the flashcards
    # dictionary
    with open('flashcards.json') as json_file:
        flashcards = json.load(json_file)

def clear_screen():
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
    # keep looping until user enters a valid menu option
    while option not in ("1", "2", "3", "4"):
        option = input("Please enter an option number (1-4): ")
    return(option)

def process_menu_option(option):
    # execute the appropriate function for the selected menu option
    if option == str(1):
        review_flashcards()
    elif option == str(2):
        create_flashcards()
        return
    elif option == str(3):
        delete_flashcards()
    elif option == str(4):
        clear_screen()
        quit()
    

def create_flashcards():
    clear_screen()
    # keep allowing the user to create flashcards until they are done (indicated by
    # pressing the enter/return key without any other text)
    while(True):
        print("\nWhen done entering flashcards, press enter for FRONT to exit\n")
        front = input("Please enter text for flashcard FRONT (word, question, etc.: ")
        if front == "":
            return
        back = input("Please enter text for flashcard BACK (definition, answer, etc.: ")
        # add a key: value pair to the flashcards dictionary
        flashcards[front] = back
        # write the new version of the flashcards json file to disk
        # from the dictionary
        with open('flashcards.json', 'w') as outfile:
            json.dump(flashcards, outfile)
        # prepare for entering the next flashcard
        clear_screen()
        front = ""
        back = ""
        
def review_flashcards():
    # used for iterating through flashcard dictionary
    length = len(flashcards)
    # used for printing dashes across the screen to separate the 
    # flashcard front/back from instructions to the user (below the) 
    # dashed line
    width = 72
    # extract the dictionary keys to a list
    key_list = list(flashcards.keys())
    # extract the dictionary values to a list
    value_list = list(flashcards.values())
    # loop through each flashcard
    for i in range(0, length):
        option = 'a'
        while option != "":
            clear_screen()
            # display the front of the current flashcard
            print(key_list[i], end = "\n\n")
            print("-"*width)
            print("Press enter/return key to see back of flashcard\n")
            option = input()
        clear_screen()
        # re-display the front of the current flashcard
        print(key_list[i], end = "\n\n")
        # display the back of the current flashcard
        print(value_list[i], end = "\n\n")
        print("-"*width)
        input_string = input("Press enter/return key for next flashcard or q to return to menu: ")
        if input_string.lower() == "q":
            return
        clear_screen()

def delete_flashcards():
    option = 'a'
    key_to_delete = -1
    clear_screen()
    # display a list of numbered flashcard keys
    for i,j in enumerate(flashcards):
        print(f"Index: {i}, Key: {j}")
    print("\n")
    # make sure the user enters digit(s) so it can be converted to an integer index number
    while not option.isdigit():
        option = input("Enter index to be deleted or press enter/return to exit without deleting: ")
        if option == "":
            return
    index_to_delete = int(option)
    # save the dictionary keys to a list (key_list)
    key_list = list(flashcards.keys())
    # make sure the user entered a valid index number 
    if index_to_delete < len(key_list):
        key_to_delete = (key_list[index_to_delete])
    else:
        input("Invalid key entered, press enter/return to return to menu")
        return
    # make sure they have selected the one they want to delete
    confirm_delete = input(f"DELETE Index: {index_to_delete}, Key: {key_to_delete}? (y/n) ")
    if confirm_delete.lower() != 'y':
        return
    # delete the desired flashcard from the dictionary
    flashcards.pop(key_to_delete, None)
    # write the updated dictionary to the json file
    with open('flashcards.json', 'w') as outfile:
        json.dump(flashcards, outfile)
    
if __name__ == '__main__':
    sys.exit(main()) 
