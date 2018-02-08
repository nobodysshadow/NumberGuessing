#Imports and #Import doctype
"""
Import randomize library int
"""
from random import randint

#guess_number.py Application
"""
The first small and simple project to have an app that selects a random number between 1 and 99.
The player has a maximum of five guesses to find the selected number.
By each Guess you will get a feedback if the selected number is bigger or smaller than your guess.
Hope you find it interessting.
"""

#Testing it is the right value
def get_number(comment):
    """
    Check that the input is a correct number
    comment: give the text to ask for the number.
    """
    while True:
        try:
            number = int(input(comment))
        except Exception:
            print("This was no number!")
        finally:
            break
    return number

# Get the Settings for the game
def get_settings():
    #Function doctype
    """
    get_settings will return the limits of the game
    returns the lowest possible, the highest possible number and the number of tries
    """
    print("Please provide the range first.")
    settings = ["Lowest possible number: ", "Highest possible number: ", "Number of tries: "]
    save_settings = []
    for i in settings:
        # print(i)
        save_settings.append(get_number(i))
        # print(save_settings)
    return save_settings

#Function that find give a rand number
def set_number(lowest, highest):
    #Function doctype
    """
    get_number generates the random number within the given limits
    lowest: The lowest possible number
    highest: The highest possible number
    """
    return randint(lowest, highest)

#Function that ask for the try and check if it is the number
def check_number(number, randomint):
    #Function doctype
    """
    Here the player is actually guessing and the answer get compared.
    number: The number that should be verified against
    randomint: The random integer the user must guess
    """
    #Check the number
    if number == randomint:
        print("You have guessed the correct answer!")
        success = 1
    elif number > randomint:
        print("It's not the correct number. You guessed to big.")
        success = 0
    else:
        print("It's not the correct number. You guessed to small.")
        success = 0
    return success

#Ask the settings of the game
print("Welcome to Guess Number, a game to guess a number within a range.")
SAVE_SETTINGS = get_settings()
COUNT = 0
TO_FIND = set_number(SAVE_SETTINGS[0], SAVE_SETTINGS[1])

#run the main game
while SAVE_SETTINGS[2] > COUNT:
    GUESS = get_number("Your Guess: ")
    COUNT = COUNT + 1
    if check_number(GUESS, TO_FIND) == 1:
        break
    else:
        TEXT1 = "Try again. You have "
        TEXT2 = str((SAVE_SETTINGS[2] - COUNT)) + " remaining guesses"
        print(TEXT1 + TEXT2)
        print(" ")

#Ending
if COUNT > SAVE_SETTINGS[2]:
    print("Good luck next time.")
input("Press ENTER to close the programm!")
