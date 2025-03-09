from AppAPI import *
from globalvars import *
from EPDAPI import *
from samsungtvws import SamsungTVWS
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
        self.TVApp.settingsManager.setSetting("ip", ipToStr(ip))
        self.tv.close()
        self.tv = SamsungTVWS(
            name = self.TVApp.settingsManager.getSetting("name"),
            host = self.TVApp.settingsManager.getSetting("ip"),
            port = self.TVApp.settingsManager.getSetting("port"),
            token_file = self.TVApp.settingsManager.getSetting("token_file")
        )
        
    
    def __init__(self):
        self.TVApp = App("samsungtv", "SamsungTV", usesWifi = True, name = "glove", ip = "192.168.86.24", token_file = os.path.dirname(os.path.realpath(__file__)) + '/samsungtvtoken.txt', port = 8002)
        
        
        
        self.tv = SamsungTVWS(
            name = self.TVApp.settingsManager.getSetting("name"),
            host = self.TVApp.settingsManager.getSetting("ip"),
            port = self.TVApp.settingsManager.getSetting("port"),
            token_file = self.TVApp.settingsManager.getSetting("token_file")
        )
               
        
        
        # TVAPP.settingsManager.getSetting("ip")
        self.TVApp.setAppCommand(self.tv.shortcuts().home, "IT")
        self.TVApp.setAppCommand(self.tv.shortcuts().left, "IM")
        self.TVApp.setAppCommand(self.tv.shortcuts().volume_down, "IB")
        self.TVApp.setAppCommand(self.tv.shortcuts().up, "MT")
        self.TVApp.setAppCommand(self.tv.shortcuts().enter, "MM")
        self.TVApp.setAppCommand(self.tv.shortcuts().down, "MB")
        self.TVApp.setAppCommand(self.tv.shortcuts().back, "RT")
        self.TVApp.setAppCommand(self.tv.shortcuts().right, "RM")
        self.TVApp.setAppCommand(self.tv.shortcuts().volume_up, "RB")
        self.TVApp.setAppCommand(self.tv.shortcuts().power, "PT")
        self.TVApp.setAppCommand(self.changeIP, "PB")
        
        
