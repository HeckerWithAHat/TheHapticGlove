from globalvars import *

class App:
    
    # init method takes unspecified keyword args amount and assigns the outputted dictionary to appDefinedCommands, which is formatted as
    # {commandId: {name: name, method:method}}
    # {settingId: {name: name, Setting:Setting}}
    # Make Setting class
    def __init__(self, appId, name):
        installed_apps[str(appId)] = self
        self.appName = name
        self.appDefinedCommands = {}
        
    def setAppCommands(self, func, button = "", usesWifi = False):
        self.appDefinedCommands[button] = func
        
        
    def setAppSettings(self, **settings):
        self.appDefinedSettings = settings
    
    def setAppName(self, name):
        self.appName = name
        
    
    def assignToButton(self, commandId, LocationToPut):
        buttonNumber = self.string_to_number(LocationToPut)
        current_buttons[str(buttonNumber)] = self.appDefinedCommands[commandId]["method"]
    
    
    