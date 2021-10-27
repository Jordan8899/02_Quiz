
# Function
def statement_decoration(statement, decoration):

    # How much decoration is on either side of the statement
    sides = decoration * 3

    # Defines where the sides and statement are
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    # Prints the decoration as well as the statement
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main Routine
statement_decoration("hi", "*")
