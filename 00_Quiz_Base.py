
# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

    # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter either \"Yes\" or \"No\"")

def instructions():
    print("***** How to play *****")
    print("")
    print("Instructions go here")
    print("")
    print("***********************")
    print("")
    return ""

def gamemode():
    i = True
    print("This quiz has multiple gamemode having: 'timed', 'difficult', 'easy'")
    while i:
        gamemode_selection = input("What gamemode would you like to select? ")
        gamemode_selection = gamemode_selection.strip().lower()
        if gamemode_selection == "timed":
            print("You have selected the timed gamemode")
            i = False

        elif gamemode_selection == "difficult":
            print("You have selected the difficult gamemode")
            i = False

        elif gamemode_selection == "easy":
            print("You have selected the easy gamemode")
            i = False

        else:
            print("Please select one of the following gamemodes: 'timed' 'difficult' 'easy'")


# Main routine
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

gamemode()

print("Game Starts")
