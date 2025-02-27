from AppAPI import *
from globalvars import *
from EPDAPI import *
from samsungtvws import SamsungTVWS
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
        self.tv = SamsungTVWS(
            name = "glove",
            host= self.ip,
            port=8002,
            token_file=self.token_file
        )
        
    
    def __init__(self):
        self.ip = ""
        self.token_file = os.path.dirname(os.path.realpath(__file__)) + '/samsungtvtoken.txt'
        self.tv = SamsungTVWS(
            name = "glove",
            host= self.ip,
            port=8002,
            token_file=self.token_file
        )
               
        
        TVApp = App("samsungtv", "SamsungTV")
        TVApp.setAppCommand(self.tv.shortcuts().home, "IT")
        TVApp.setAppCommand(self.tv.shortcuts().left, "IM")
        TVApp.setAppCommand(self.tv.shortcuts().volume_down, "IB")
        TVApp.setAppCommand(self.tv.shortcuts().up, "MT")
        TVApp.setAppCommand(self.tv.shortcuts().enter, "MM")
        TVApp.setAppCommand(self.tv.shortcuts().down, "MB")
        TVApp.setAppCommand(self.tv.shortcuts().back, "RT")
        TVApp.setAppCommand(self.tv.shortcuts().right, "RM")
        TVApp.setAppCommand(self.tv.shortcuts().volume_up, "RB")
        TVApp.setAppCommand(self.tv.shortcuts().power, "PT")
        TVApp.setAppCommand(self.changeIP, "PB")