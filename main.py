gamemode = False
while not gamemode:
    gamemode = input("Gamemode? ")
    gamemode = gamemode.strip().lower()
    if gamemode == "hard":
        gamemode = True
    elif gamemode == "easy":
        gamemode = True
    elif gamemode == "timed":
        gamemode = True
    else:
        print("Please input")
        gamemode = False
