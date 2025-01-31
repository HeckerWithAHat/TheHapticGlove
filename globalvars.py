wifiModeActive = False
getOpenApp = ""
config_buttons = {
    "IT": "",
    "IM": "", # LEFT
    "IB": "",
    "MT": "", # UP
    "MM": "", # SELECT
    "MB": "", # DOWN
    "RT": "",
    "RM": "", # RIGHT
    "RB": "",
    "PT": "",
    "PB": ""
}
current_buttons = {
    
}


long_buttons = {
    "0": "",
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": ""
}
installed_apps = {}
epd = None
chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=~`[]{}|\\:;"\'<>,.?/ ')
buttons = {}
def fingerCodeToNumber(self, s):
        return mapping.get(s.upper(), None)
mapping = {
    'PT': 38, 'PB': 40, 'RB': 37, 'RM': 35, 'RT': 33,
    'MB': 12, 'MM': 10, 'MT': 8, 'IB': 7, 'IM': 5, 'IT': 3
}
