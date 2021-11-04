
# List of game modes
print("This quiz has multiple gamemode having: 1 'hard', 2 'normal', 3 'easy'")

# Select Game Mode
gamemode_selection = input("What gamemode would you like to select? ")

# If statement that prints if the user inputted hard
if gamemode_selection == "1" or "hard":
    print("You have selected the hard gamemode")

# Elif statement that prints if the user inputted normal
elif gamemode_selection == "2" or "normal":
    print("You have selected the normal gamemode")

# Elif statement that prints if the user inputted easy
elif gamemode_selection == "3" or "easy":
    print("You have selected the easy gamemode")

# Tells the user they didn't input a valid gamemode and stops the code
else:
    print("You have not selected a gamemode")
