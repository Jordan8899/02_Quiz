
# List of game modes
print("This quiz has multiple gamemode having: 'timed', 'difficult', 'easy'")

# Select Game Mode
def gamemode():
    i = True
    while i:
        gamemode_selection = input("What gamemode would you like to select? ")

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

gamemode()
