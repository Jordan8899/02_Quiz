
# Select Game Mode
def gamemode():
    i = True
    while i:
        gamemode = input("\nWhat difficulty would you like to select? The options are: {} ".format(gamemode_options))
        gamemode = gamemode.replace(" ", "").lower()
        if gamemode == "hard":
            i = False
        elif gamemode == "easy":
            i = False
        elif gamemode == "normal":
            i = False
        else:
            print("Please input either 'easy', 'normal', or 'hard'")


gamemode_options = ["Easy", "Normal", "Hard"]

# Try and fix it
if gamemode == "hard":
    print("Hard")
elif gamemode == "normal":
    print("Normal")
elif gamemode == "easy":
    print("Easy")
else:
    print("{}".format(gamemode))
