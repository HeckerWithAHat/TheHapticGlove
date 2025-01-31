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
buttons = []
def fingerCodeToNumber(self, s):
        return mapping.get(s.upper(), None)
mapping = {
    'PB': 15, 'PT': 14, 'RB': 9, 'RM': 11, 'RT': 10,
    'MB': 8, 'MM': 7, 'MT': 6, 'IB': 4, 'IM': 3, 'IT': 2
}