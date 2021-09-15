
# List of game modes
print("This quiz has multiple gamemode having: 1 'timed', 2 'difficult', 3 'easy'")

# Select Game Mode
gamemode_selection = input("What gamemode would you like to select? ")

if gamemode_selection == "1" or "timed":
    print("You have selected the timed gamemode")

elif gamemode_selection == "2" or "difficult":
    print("You have selected the difficult gamemode")

elif gamemode_selection == "3" or "easy":
    print("You have selected the easy gamemode")

else:
    print("You have not selected a gamemode")
