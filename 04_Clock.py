import time
countdown = 10
# Functions goes here


# Main Routine goes here
print(countdown)
while time:
    countdown = countdown - 1
    time.sleep(1)
    print(countdown)
    if countdown == 0:
        time = False
