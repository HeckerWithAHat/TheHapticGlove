from LCDAPI.I2C_LCD import I2CLcd
from machine import I2C, Pin
screen = I2CLcd(I2C(0, sda=Pin(20), scl=Pin(21), freq=400000), I2C(0, sda=Pin(20), scl=Pin(21), freq=400000).scan()[0], 2, 16)
current_buttons = {
    "IT": "",
    "IM": "",
    "IB": "",
    "MT": "",
    "MM": "",
    "MB": "",
    "RT": "",
    "RM": "",
    "RB": "",
    "PT": "",
    "PB": ""
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