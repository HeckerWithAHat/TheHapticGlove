from globalvars import * 
from time import sleep
import network
import os

class OS:
    def __init__(self, wifi_SSID, wifi_PASS):
        screen.putstr("Glove OS Booting")
        screen.move_to(0,1)
        screen.putstr("Starting...")
        sleep(1)
        self.connectToWiFi(wifi_SSID,wifi_PASS)
        sleep(1)
        self.registerApps()
        sleep(1)
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Glove OS Booting")
        screen.move_to(0,1)
        screen.putstr("Done!")
        sleep(1)
        screen.clear()
        
    
    def connectToWiFi(self, name, password):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        networks = wlan.scan()
        for networkinlist in networks:
            print(networkinlist[0])
        wlan.connect(name, password)
        while wlan.isconnected() == False:
            screen.move_to(0, 1)
            screen.putstr("WiFi Connecting")
            sleep(0.2)
        screen.move_to(0, 1)
        screen.putstr("Connected       ")
        sleep(1)
        screen.move_to(0, 1)
        screen.putstr(wlan.ifconfig()[0])
    
    def registerApps(self):
        screen.move_to(0, 1)
        screen.putstr("Registering Apps")
        sleep(1)
        count = 0
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Glove OS Booting")
        screen.move_to(0, 1)
        screen.putstr(str(count) + " Registered")
        for file_name in os.listdir("apps"):
            if file_name.endswith(".py"):
                class_name = file_name[:-3]  # Remove the .py extension
                classToRegister = getattr(__import__('apps.' + class_name, globals(), locals(), [class_name], 0), class_name)
                
                instance = classToRegister()
                count = count + 1
                screen.move_to(0, 1)
                screen.putstr(str(count) + " Registered")
