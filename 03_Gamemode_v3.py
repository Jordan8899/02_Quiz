
# Select Game Mode
def gamemode():
    i = False
    while not i:
        gamemode = input("What gamemode would you like to select, 'hard' or 'easy'? ")
        gamemode = gamemode.strip().lower()
        if gamemode == "hard":
            i = True
        elif gamemode == "easy":
            i = True
        else:
            print("Please input")
            i = False
gamemode()

print(gamemode)

# This is broken use the 05_Questions_v2 instead
