import subprocess
import os
import time
import epd2in13b_V4
import globalvars
from gpiozero import *
import nmcli
class OS:
    def __init__(self):
        # If yes do all the wifi stuff, and set the wifi variable in global vars to true
        # If no, just boot up the OS, and set the wifi variable in global vars to false
        for m in globalvars.mapping: 
            globalvars.buttons[m] = Button(globalvars.mapping[m])
        globalvars.epd = epd2in13b_V4.EPD()
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
                    lines = subprocess.check_output(["iwlist", "wlan0", "scan"]).decode("utf-8").split('\n')
                    print(lines)
                    ssids = set()
                    for line in lines:
                        if "ESSID:" in line:
                            ssid = line.split("ESSID:")[-1].strip()
                            ssids.add(ssid)
                    ssids = sorted(list(ssids))
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
                    currentPlace = (0,0)
                    charList = [list('ABCDEFGHIJKLM!@#$%^'),list('NOPQRSTUVWXYZ&*()-_'),list('abcdefghijklm+=~`[]'),list('nopqrstuvwxyz{}|\\:;'),list('0123456789"\'<>,.?/ ')]
                    EPDAPI.createKeyboardFromPrompt("What is the password?", charList[currentPlace[0]][currentPlace[1]])
                    # read input and update the currentChar, then when select is pressed, add current char to wifi_PASS
                    currenttext = ""
                    while wifi_PASS == "":
                        if globalvars.buttons["IM"].is_pressed: # left
                            currentPlace = (currentPlace[0], (currentPlace[1] - 1) % 19)
                            print(currentPlace)
                            EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext, charList[currentPlace[0]][currentPlace[1]])
                        if globalvars.buttons["MM"].is_pressed: # select
                            currenttext +=charList[currentPlace[0]][currentPlace[1]]
                            EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext, charList[currentPlace[0]][currentPlace[1]])
                        if globalvars.buttons["RM"].is_pressed: # right
                            currentPlace = (currentPlace[0], (currentPlace[1] + 1) % 19)
                            print(currentPlace)
                            EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext, charList[currentPlace[0]][currentPlace[1]])
                        if globalvars.buttons["MT"].is_pressed: # up
                            currentPlace = ((currentPlace[0] - 1) % 5, currentPlace[1])
                            print(currentPlace)
                            EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext, charList[currentPlace[0]][currentPlace[1]])
                        if globalvars.buttons["MB"].is_pressed: # down
                            currentPlace = ((currentPlace[0] + 1) % 5, currentPlace[1])
                            print(currentPlace)
                            EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext, charList[currentPlace[0]][currentPlace[1]])
                        if globalvars.buttons["IT"].is_pressed: # YES
                            wifi_PASS = currenttext
                            break
                        if globalvars.buttons["RT"].is_pressed: # back
                            currenttext = currenttext[:-1] 
                            EPDAPI.createKeyboardFromPrompt("What is the password: " + currenttext, charList[currentPlace[0]][currentPlace[1]])

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
        
        count = 0
        for file_name in os.listdir("apps"):
            if file_name.endswith(".py"):
                class_name = file_name[:-3]  # Remove the .py extension
                classToRegister = getattr(__import__('apps.' + class_name, globals(), locals(), [class_name], 0), class_name)
                
                instance = classToRegister()
                count = count + 1
                
