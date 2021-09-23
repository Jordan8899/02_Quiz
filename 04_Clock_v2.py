# import the time module
import time
  
# define the countdown func.
def countdown(count):

    while count:
        minutes, secs = divmod(count, 60)
        timer = "{:02d}:{:02d}".format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        count -= 1

    print("Times Up")


# The time limit before Times Up
t = 5

# Question that calls function
question = int(input("What is 2 + 3 "))
while question != 5:
    countdown(int(t))
