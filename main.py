import sys
import network
from time import sleep
from gpiozero import Button
import urequests
from globalvars import * 
from AppAPI import App
from OS import OS






operatingSystem = OS()



installed_apps["spotify"].assignToButton("playpause", "IT")
installed_apps["spotify"].assignToButton("shuffletoggle", "IM")
installed_apps["spotify"].assignToButton("repeattoggle", "IB")
installed_apps["spotify"].assignToButton("skipsong", "MB")
installed_apps["spotify"].assignToButton("previoussong", "RB")
installed_apps["spotify"].assignToButton("volumeup", "MT")
installed_apps["spotify"].assignToButton("volumedown", "MM")
installed_apps["stopwatch"].assignToButton("startCheckStopwatch", "PT")
installed_apps["stopwatch"].assignToButton("pauseStopStopwatch", "PB")

for x in range(12):
    button = Button(x)
    button.when_pressed = current_buttons[str(x)]



