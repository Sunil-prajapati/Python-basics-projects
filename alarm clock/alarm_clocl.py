from playsound3 import playsound
import time
import os

CLEAR = "\033[23"
CLEAR_AND_RETURN = "\033[H"
print(os.getcwd())
def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alaram will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 * seconds
alarm(10)
