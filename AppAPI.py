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
        
        settings = json.load(open("settings.json"))
        if self.appId in settings.keys():
            return settings[self.appId]
        else:
            with open("settings.json", "w") as settingsFile:
                settings[self.appId] = defaultSettings
                json.dump(settings, settingsFile)
                return defaultSettings
    def getSetting(self, setting):
        return self.settings[setting]
    
    def setSetting(self, setting, value):
        self.settings[setting] = value
        with open("settings.json", "r") as settingsFile:
            data = json.load(settingsFile)
        data[self.appId] = self.settings
        with open("settings.json", "w") as settingsFile:
            json.dump(data, settingsFile)
            
# sm = SettingsManager("test", test = "test", test2 = 2, test3 = True)
# print(sm.settings)
# print(sm.getSetting("test"))
# print(sm.getSetting("test2"))
# print(sm.getSetting("test3"))
# sm.setSetting("test", "new test")
# print(sm.getSetting("test"))
# print(sm.getSetting("test2"))
# print(sm.getSetting("test3"))
# sm = SettingsManager("test", test = "test", test2 = 2, test3 = True)
# print(sm.settings)