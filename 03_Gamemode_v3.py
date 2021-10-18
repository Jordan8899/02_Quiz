
# Select Game Mode
def gamemode():
    i = False
    while not i:
        gamemode_user = input("What gamemode would you like to select, 'hard' or 'easy'? ")
        gamemode_user = gamemode_user.strip().lower()
        if gamemode_user == "hard":
            i = True
        elif gamemode_user == "easy":
            i = True
        else:
            print("Please input")
            i = False
gamemode()

print(gamemode)

# This is broken use the 05_Questions_v2 instead
