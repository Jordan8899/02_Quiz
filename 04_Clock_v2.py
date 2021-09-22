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


# input time in seconds
t = 5

# function call
countdown(int(t))
