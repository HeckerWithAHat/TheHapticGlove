from AppAPI import *
from globalvars import *
from EPDAPI import *
from samsungctl import Remote, Config 
import socket
class SamsungApp:
    
    def changeIP(self):
        savedButtons = globalvars.current_buttons
        globalvars.current_buttons = {}
        ip = []
        def ipToStr(ip) :
            if len(ip) == 0:
                return ""
            if len(ip) == 1:
                return str(ip[0]) + "."
            if len(ip) == 2:
                return str(ip[0]) + "." + str(ip[1]) + "."
            if len(ip) == 3:
                return str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "."
            return str(ip[0]) + "." + str(ip[1]) + "." + str(ip[2]) + "." + str(ip[3])
        currentNum = ""
        createNumpadFromPrompt("What is the IP address: ")
        # read input and update the currentChar, then when select is pressed, add current char to wifi_PASS
        while len(ip) < 4:
            numrn = currentNum
            if globalvars.buttons["IT"].is_pressed: # 1
                currentNum += "1"
            elif globalvars.buttons["IM"].is_pressed: # 2
                currentNum += "2"
            elif globalvars.buttons["IB"].is_pressed: # 3
                currentNum += "3"
            elif globalvars.buttons["MT"].is_pressed: # 4
                currentNum += "4"
            elif globalvars.buttons["MM"].is_pressed: # 5
                currentNum += "5"
            elif globalvars.buttons["MB"].is_pressed: # 6
                currentNum += "6"
            elif globalvars.buttons["RT"].is_pressed: # 7
                currentNum += "7"
            elif globalvars.buttons["RM"].is_pressed: # 8
                currentNum += "8"
            elif globalvars.buttons["RB"].is_pressed: # 9
                currentNum += "9"
            elif globalvars.buttons["PT"].is_pressed: # 0
                currentNum += "0"
            elif globalvars.buttons["PB"].is_pressed: # next
                ip.append(currentNum)
                currentNum = ""
            if len(currentNum) > 3:
                currentNum = currentNum[(len(currentNum)-3):]
            if currentNum != numrn:
                createNumpadFromPrompt("What is the IP address: " + ipToStr(ip)+currentNum)
        globalvars.current_buttons = savedButtons
        print(ipToStr(ip))
        self.ip = ipToStr(ip)
        
    def home(self):
        with Remote(self.config) as remote:
            remote.control("KEY_MENU")
    
    def left(self):
        with Remote(self.config) as remote:
            remote.control("KEY_LEFT")
            
    def volume_down(self):
        with Remote(self.config) as remote:
            remote.control("KEY_VOLDOWN")
            
    def up(self):
        with Remote(self.config) as remote:
            remote.control("KEY_UP")
            
    def enter(self):
        with Remote(self.config) as remote:
            remote.control("KEY_ENTER")
            
    def down(self):
        with Remote(self.config) as remote:
            remote.control("KEY_DOWN")
            
    def back(self):
        with Remote(self.config) as remote:
            remote.control("KEY_RETURN")
            
    def right(self):
        with Remote(self.config) as remote:
            remote.control("KEY_RIGHT")
            
    def volume_up(self):
        with Remote(self.config) as remote:
            remote.control("KEY_VOLUP")
            
    def power(self):
        with Remote(self.config) as remote:
            remote.control("KEY_POWER")
    
    def __init__(self):
        self.ip = "192.186.86.24"
        self.config = Config(
            name = "samsungctl",
            description= "glove",
            host= self.ip,
            method= "websocket"
        )
               
        
        TVApp = App("samsungtv", "SamsungTV")
        TVApp.setAppCommand(self.home, "IT")
        TVApp.setAppCommand(self.left, "IM")
        TVApp.setAppCommand(self.volume_down, "IB")
        TVApp.setAppCommand(self.up, "MT")
        TVApp.setAppCommand(self.enter, "MM")
        TVApp.setAppCommand(self.down, "MB")
        TVApp.setAppCommand(self.back, "RT")
        TVApp.setAppCommand(self.right, "RM")
        TVApp.setAppCommand(self.volume_up, "RB")
        TVApp.setAppCommand(self.power, "PT")
        TVApp.setAppCommand(self.changeIP, "PB")
        
        

    

