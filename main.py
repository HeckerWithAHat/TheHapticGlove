import sys
import network
from time import sleep
from machine import Pin, Timer
import urequests
from globalvars import * 
from AppAPI import App
from OS import OS






operatingSystem = OS("Aryan iPhone", "AryanJain1010")



installed_apps["spotify"].assignToButton("playpause", "IT")
installed_apps["spotify"].assignToButton("shuffletoggle", "IM")
installed_apps["spotify"].assignToButton("repeattoggle", "IB")
installed_apps["spotify"].assignToButton("skipsong", "MB")
installed_apps["spotify"].assignToButton("previoussong", "RB")
installed_apps["spotify"].assignToButton("volumeup", "MT")
installed_apps["spotify"].assignToButton("volumedown", "MM")
installed_apps["stopwatch"].assignToButton("startCheckStopwatch", "PT")
installed_apps["stopwatch"].assignToButton("pauseStopStopwatch", "PB")

# Define what happens when the button is pressed
def on_press(pin_num):
    whatToRun = current_buttons[str(pin_num)]
    whatToRun()
    print(str(pin_num) + " pressed")

def checkpressed(t):
    for x in range(12):
        button = machine.Pin(x, machine.Pin.IN, machine.Pin.PULL_UP)

        # Read the button state
        button_state = button.value()
    
        if button_state == 0:
            on_press(x)
        # Wait for a short period before checking again

timer = Timer(period=125, callback=checkpressed)



