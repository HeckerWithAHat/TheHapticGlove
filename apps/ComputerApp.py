from AppAPI import *
from globalvars import *
from EPDAPI import *
import websocket
class ComputerApp:
    
    
    
    def __init__(self):
        self.computerApp = App("computerApp", "Computer Controller", True, token="", ip="192.168.86.25", port=8000)
        self.computerApp.setAppCommand(self.mouseul, "IT")
        self.computerApp.setAppCommand(self.mousel, "IM")
        self.computerApp.setAppCommand(self.mousedl, "IB")
        self.computerApp.setAppCommand(self.mouseu, "MT")
        self.computerApp.setAppCommand(self.mousetoggle, "MM")
        self.computerApp.setAppCommand(self.moused, "MB")
        self.computerApp.setAppCommand(self.mouseur, "RT")
        self.computerApp.setAppCommand(self.mouser, "RM")
        self.computerApp.setAppCommand(self.mousedr, "RB")
        self.computerApp.setAppCommand(self.clickl, "PT")
        self.computerApp.setAppCommand(self.clickr, "PB")
        self.connection = websocket.create_connection(f"ws://{self.computerApp.settingsManager.getSetting('ip')}:{self.computerApp.settingsManager.getSetting('port')}")
        self.connection.send("auth")
        result = self.connection.recv()
        if result == "auth:failed":
            self.computerApp.settingsManager.setSetting("token", "")
        else: 
            token = result.split("&")[1].split(":")[1]
            self.computerApp.settingsManager.setSetting("token", token)
    
    def mouseu(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemoveup")
    def moused(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemovedown")
    def mousel(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemoveleft")
    def mouser(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemoveright")
    def mouseul(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemoveupleft")
    def mousedl(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemovedownleft")
    def mouseur(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemoveupright")
    def mousedr(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousemovedownright")
    def mousetoggle(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mousedowntoggle")
    def clickl(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mouseleftclick")
    def clickr(self):
                self.connection.send("token:" + self.computerApp.settingsManager.getSetting("token") + "&command:mouserightclick")
