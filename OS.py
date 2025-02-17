import subprocess
import os
import time
import epd2in13_V4
import globalvars
from gpiozero import *
import nmcli
class OS:
    def __init__(self):
        # If yes do all the wifi stuff, and set the wifi variable in global vars to true
        # If no, just boot up the OS, and set the wifi variable in global vars to false
        for m in globalvars.mapping: 
            globalvars.buttons[m] = Button(globalvars.mapping[m])
        globalvars.epd = epd2in13_V4.EPD()
        globalvars.epd.init()
        globalvars.epd.Clear()
        time.sleep(1)
        import EPDAPI
        
        EPDAPI.createImageFromOptions("Do you want to use WiFi?", ["Yes", "No"])
        usingWifi = None
        while usingWifi == None:
            if globalvars.buttons["IT"].is_pressed: # YES
                usingWifi = True
            if globalvars.buttons["RT"].is_pressed: # NO
                usingWifi = False
                break
        globalvars.wifiModeActive = usingWifi
        didWifiConnect = False
        if globalvars.wifiModeActive:
            changeWifi = None
            EPDAPI.createImageFromOptions("Do you want to change WiFi?", ["Yes", "No"])
            while changeWifi == None:
                if globalvars.buttons["IT"].is_pressed: # YES
                    changeWifi = True
                if globalvars.buttons["RT"].is_pressed: # NO
                    changeWifi = False
                    break
            if changeWifi:
                while didWifiConnect == False:
                    wifi_SSID = ""
                    ssids = list()
                    for wifi in nmcli.device.wifi():
                        ssids.append(wifi.ssid)
                    ssids = sorted(list(set(ssids)))
                    print(ssids)
                    EPDAPI.createImageFromOptions("What is the name of the WiFi?", ssids)
                    while wifi_SSID == "":
                        if globalvars.buttons["IM"].is_pressed: # left
                            ssids.append(ssids.pop(0))
                                
                        if globalvars.buttons["MM"].is_pressed: # select
                            wifi_SSID = ssids[0]
                            break
                        if globalvars.buttons["RM"].is_pressed: # right
                            ssids.insert(0,ssids.pop())
                    wifi_PASS = ""
                    currentPlace = (2,9)
                    charList = [list('ABCDEFGHIJKLM!@#$%^'),list('NOPQRSTUVWXYZ&*()-_'),list('abcdefghijklm+=~`[]'),list('nopqrstuvwxyz{}|\\:;'),list('0123456789"\'<>,.?/ ')]
                    baseImage = EPDAPI.createKeyboardFromPrompt("What is the password?")
                    EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "up")
                    # read input and update the currentChar, then when select is pressed, add current char to wifi_PASS
                    currenttext = ""
                    while wifi_PASS == "":
                        if globalvars.buttons["IM"].is_pressed: # left
                            currentPlace = (currentPlace[0], (currentPlace[1] - 1) % 19)
                            print(currentPlace)
                            EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "left")
                        if globalvars.buttons["MM"].is_pressed: # select
                            currenttext +=charList[currentPlace[0]][currentPlace[1]]
                            baseImage = EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext)
                            EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "up")

                        if globalvars.buttons["RM"].is_pressed: # right
                            currentPlace = (currentPlace[0], (currentPlace[1] + 1) % 19)
                            print(currentPlace)
                            EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "right")
                        if globalvars.buttons["MT"].is_pressed: # up
                            currentPlace = ((currentPlace[0] - 1) % 5, currentPlace[1])
                            print(currentPlace)
                            EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "up")
                        if globalvars.buttons["MB"].is_pressed: # down
                            currentPlace = ((currentPlace[0] + 1) % 5, currentPlace[1])
                            print(currentPlace)
                            EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "down")
                        if globalvars.buttons["PT"].is_pressed: # YES
                            wifi_PASS = currenttext
                            break
                        if globalvars.buttons["PB"].is_pressed: # back
                            currenttext = currenttext[:-1] 
                            baseImage = EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext)
                            EPDAPI.updateKeyboardFromPrompt(baseImage, currentPlace, "up")



                    self.changeWifi(wifi_SSID, wifi_PASS)
                    didWifiConnect = self.connectedToWiFi()
            else:
                didWifiConnect = self.connectedToWiFi()
    
        
    def changeWifi(self, name, password):
        # Disconnect from current network
        nmcli.radio.wifi_off()
        nmcli.radio.wifi_on()
        newWifi = True  
        conns = nmcli.connection()
        for conn in conns:
            if conn.name == name:
                newWifi = False
                break
        if newWifi:
            nmcli.connection.up(name)
        else:
            nmcli.device.wifi_connect(name, password)
        
    def connectedToWiFi(self):

        # Get the current IP address
        result = subprocess.run(['hostname', '-I'], capture_output=True)
        print(result)
        print(result.stdout)
        ip_address = str(result.stdout).split()[0]

        if ip_address:
            print(f"Connected to Wi-Fi. Current IP: {ip_address}")
            return True
        else:
            print("Failed to connect to Wi-Fi. Attempting to update Wi-Fi settings.")
            return False
    
    def registerApps(self):
        # register/initialize all apps
        # store in a list in global vars
        pass
        
    def changeApp(self):
        # using the list of all apps in global vars, display imageFromOptions of all apps that are available
        # available apps are ones that fit the current mode (wifi or not)
        # listen for button presses and change the current app to the selected app
        # on select, change the current commands to the selected app's commands
        
        # this command should be called when both the index and middle finger and pressed and held
        pass    
    
    def changeSetting(self):
        # using the list of all apps in global vars, display imageFromOptions of all apps
        # listen for button presses
        # on select, using the list of all settings in global vars, display imageFromOptions of all settings
        # listen for button presses and change the current setting to the option selected
        # Setting is a JSON file of all the required information about setting
        # Setting = {name: name, type: toggle/keyboard/option, value: value}
        
        # this command should be called when both the ring and pinky finger and pressed and held
        pass
                
