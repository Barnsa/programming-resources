# example-3.py
# Simplified executable run loop 
check = True
count = 1
while check:
    if count == 1:
        print("This program will continue to run until you tell it to stop!")
        print("Do you want to stop yet?")
    if count != 1:
        print("How about now? ")
    answer = input().lower()
    stop_commands = ["stop", "exit", "yes", "sure", "get me out of here you filthy mudblood!"]
    count += 1
    if answer in stop_commands:
        answer = input("Are you sure? ").lower()
        if answer in stop_commands:
            break 