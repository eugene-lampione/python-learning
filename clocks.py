import time
from datetime import datetime
import os
import threading 
from zoneinfo import ZoneInfo
# pip install tzdata


# clear screen
def clearScreen():
    os.system("clear")

#wait for user to hit enter
def input_thread(stop_event):
    input()
    stop_event.set()

def main():
    #set up time zones
    time_zones = {
        1:("Eastern Time", "America/New_York"),
        2:("Central Time", "America/Chicago"),
        3:("Pacific Time", "America/Los_Angeles"),
    }

    # prompt user to pick a time zoe
    print("Select a time zone:")

    # Loop through timezone dictionary
    # _ is not pulling second item only first and using name as variable
    for key, (name, _) in time_zones.items():
        print(f"{key}. {name}")

    # Assign selection to variable
    choice = int(input("Enter the number of your choice: ").strip())

    # error handling for chocie
    if choice not in time_zones:
        print("Invalid Choice. Defaulting to Eastern Time.")
        tz_name = "America/New_York"
        tz_display_name = "Eastern Time"
    else:
        tz_display_name, tz_name = time_zones[choice]


    # create an event when to stop clock
    stop_event = threading.Event()

    #start the input thread
    thread = threading.Thread(target=input_thread,args=(stop_event, ))
    thread.daemon = True
    thread.start()



    #loop to update seconds
    while not stop_event.is_set():
        clearScreen()
        
        # print current time
        #currentTime = time.strftime("%H:%M:%S")
        currentTime = datetime.now(ZoneInfo(tz_name)).strftime("%I:%M:%S %p")
        print(f"Current Time: {currentTime} - {tz_display_name}")
        #prompt user to stop clock
        print("Press enter to stop the clock...")
        # run the loop once per second
        time.sleep(1)

    # print end message
    print("Clock Stopped.")





# clear the screen
clearScreen()

# call main functiin
main()