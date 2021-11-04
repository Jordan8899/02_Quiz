i = True
# List of game modes
print("This quiz has multiple gamemode having: 'hard', 'normal', 'easy'")

# Select Game Mode

while i:
    # Asks the user for an input and runs it through the code stopping if valid
    gamemode_selection = input("What gamemode would you like to select? ")

    # Selects hard gamemode
    if gamemode_selection == "hard":
        print("You have selected the hard gamemode")
        i = False

    # Selects normal gamemode
    elif gamemode_selection == "normal":
        print("You have selected the normal gamemode")
        i = False

    # Selects easy gamemode
    elif gamemode_selection == "easy":
        print("You have selected the easy gamemode")
        i = False

    # Continues loop if input is not valid
    else:
        print("Please select one of the following gamemodes: 'hard' 'normal' 'easy'")
