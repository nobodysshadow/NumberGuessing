#Imports and #Import doctype
"""
Import rand int
"""
from random import randint

#Function that find give a rand number
def get_number(lowest, highest):
    #Function doctype
    """
    lowest: The lowest possible number
    highest: The highest possible number
    """
    return randint(lowest, highest)

#Function that ask for the try and check if it is the number
def get_input(randomint):
    #Function doctype
    """
    randomint: The random integer the user must guess
    """
    #Get the try
    print("Chose a number: ")
    number = int(input())
    #Check the number
    if number == randomint:
        returnvar = 1
    else:
        returnvar = 0
    return returnvar

#Testing it is the right value
def settings_test(text):
    """
    Check the settings have the correct value
    text: give the text to ask.
    """
    error = 0
    first = 1
    while True:
        if error == 0 and first != 1:
            break
        error = 0
        print(text)
        try:
            var = int(input())
        except ValueError:
            error = 1
            print("Give a number!")
        finally:
            first = 0
    return var

#Ask the settings of the game
print("Give a range:")
SETTINGS = ["Lowest possible number:", "Highest possible number:", "Number of trys:"]
SAVE_SETTINGS = []
for i in SETTINGS:
    SAVE_SETTINGS.append(settings_test(i))
COUNT = 1
RAND = get_number(SAVE_SETTINGS[0], SAVE_SETTINGS[1])

#Main game
while SAVE_SETTINGS[2]+1 > COUNT:
    if get_input(RAND) == 1:
        print("You have guessed the correct answer")
        break
    else:
        TEXT1 = "It's not the number. Try again. You have "
        TEXT2 = str((SAVE_SETTINGS[2] - COUNT)) + " guesses"
        print(TEXT1 + TEXT2)
    COUNT = COUNT + 1
#Ending
print("Good luck next time.")
print("Press any key to close the programm")
input()
