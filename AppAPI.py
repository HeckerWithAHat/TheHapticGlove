from globalvars import *

class App:
    
    
    # Make Setting class
    def __init__(self, appId, name, usesWifi = False):
        installed_apps[str(appId)] = self
        self.appName = name
        self.appDefinedCommands = {}
        self.usesWifi = usesWifi
        
    def setAppCommand(self, func, button = ""):
        self.appDefinedCommands[button] = func
           
    def setAppSettings(self, **settings):
        self.appDefinedSettings = settings
    
    def setAppName(self, name):
        self.appName = name