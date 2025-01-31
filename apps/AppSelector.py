import sys
import os
sys.path.append(os.path.abspath('./'))
import globalvars
from AppAPI import *

class AppSelector:
    def __init__(self):
        self.AppSelector = App("appsApp", "App Selector")
        self.apps = list(globalvars.installed_apps.keys())
    
    def promptOptions(self):
        pass
    
    def promptInput(self):
        pass
     
    def select(self):
        globalvars.getOpenApp = self.apps[0]
        globalvars.current_buttons = globalvars.installed_apps[self.apps[0]].appDefinedCommands

    def left(self):
        self.apps.insert(0, self.apps.pop())
        
    def right(self):
        self.apps.append(self.apps.pop(0))
            
appS = AppSelector()
print(appS.apps)
appS.left()
print(appS.apps)
appS.right()
print(appS.apps)
        
    

    