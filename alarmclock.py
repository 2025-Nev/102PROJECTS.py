import time
from playsound import playsound

# Function to set the alarm
def set_alarm():
    print("Enter the time to set the alarm in HH:MM:SS format:")
    alarm_time = input(">> ")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            playsound('alarm_sound.mp3') # You can replace the file name with your own alarm sound
            break

# Call the set_alarm function to set the alarm
set_alarm()
