from globalvars import *

class App:
    
    # init method takes unspecified keyword args amount and assigns the outputted dictionary to appDefinedCommands, which is formatted as
    # {commandId: {name: name, method:method}}
    # {settingId: {name: name, Setting:Setting}}
    # Make Setting class
    def __init__(self, appId, name):
        installed_apps[str(appId)] = self
        self.appName = name
    def setAppDefinedCommands(self, **commands):
        self.appDefinedCommands = commands
        
    def setAppDefinedSettings(self, **settings):
        self.appDefinedSettings = settings
    
    def setAppName(self, name):
        self.appName = name
        
    
    def assignToButton(self, commandId, LocationToPut):
        buttonNumber = self.string_to_number(LocationToPut)
        current_buttons[str(buttonNumber)] = self.appDefinedCommands[commandId]["method"]
    
    def string_to_number(self, s):
        mapping = {
            'PB': 15, 'PT': 14, 'RB': 9, 'RM': 11, 'RT': 10,
            'MB': 8, 'MM': 7, 'MT': 6, 'IB': 4, 'IM': 3, 'IT': 2
        }
        return mapping.get(s.upper(), None)
    