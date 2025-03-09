from globalvars import *
import json
class App:
    
    
    # Make Setting class
    def __init__(self, appId, name, usesWifi = False, **defaultSettings):
        installed_apps[str(appId)] = self
        self.appName = name
        self.appDefinedCommands = {}
        self.usesWifi = usesWifi
        self.settingsManager = SettingsManager(appId, defaultSettings=defaultSettings)
        
    def setAppCommand(self, func, button = ""):
        self.appDefinedCommands[button] = func
           
    def setAppSettings(self, **settings):
        self.appDefinedSettings = settings
    
    def setAppName(self, name):
        self.appName = name
    def getAppName(self):
        return self.appName
    
    
    

class SettingsManager:
    def __init__(self, appId, **defaultSettings):
        self.appId = appId
        self.settings = self.loadSettings(defaultSettings)
    def loadSettings(self, defaultSettings):
        
        settings = json.load(open("Settings.json"))
        if self.appId in settings.keys():
            return settings[self.appId]
        else:
            with open("Settings.json", "w") as settingsFile:
                settings[self.appId] = defaultSettings
                json.dump(settings, settingsFile)
                return defaultSettings["defaultSettings"]
    def getSetting(self, setting):
        print(self.settings)
        return self.settings[setting]
    
    def setSetting(self, setting, value):
        self.settings[setting] = value
        with open("Settings.json", "r") as settingsFile:
            data = json.load(settingsFile)
        data[self.appId] = self.settings
        with open("Settings.json", "w") as settingsFile:
            json.dump(data, settingsFile)
            
