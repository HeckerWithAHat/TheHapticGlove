import subprocess
import os
import time
import epd2in13b_V4
import globalvars
from gpiozero import *

# TODO:
# ADD A UPDATE BUTTONS METHOD


class OS:
    def __init__(self):
        # Boot up the OS
        # Ask for if the user wants to start in wifi mode
        # If yes do all the wifi stuff, and set the wifi variable in global vars to true
        # If no, just boot up the OS, and set the wifi variable in global vars to false
        for m in globalvars.mapping: 
            globalvars.buttons[m] = Button(pin="BOARD"+str(globalvars.mapping[m]))
        globalvars.epd = epd2in13b_V4.EPD()
        globalvars.epd.init()
        globalvars.epd.Clear()
        time.sleep(1)
        import EPDAPI
        EPDAPI.createImageFromOptions("Do you want to use WiFi?", option1="Yes", option2="No")
        usingWifi = None
        while usingWifi == None:
            if globalvars.buttons["IT"].is_pressed: # YES
                usingWifi = True
                didWifiConnect = self.connectToWiFi()
                while didWifiConnect == False:
                    wifi_SSID = ""
                    lines = subprocess.check_output(["iwlist", "wlan0", "scan"]).decode("utf-8").split('\n')
                    ssids = set()
                    for line in lines:
                        if "ESSID:" in line:
                            ssid = line.split("ESSID:")[-1].strip()
                            ssids.add(ssid)
                    ssids = sorted(list(ssids))
                    EPDAPI.createImageFromOptions("What is the name of the WiFi?", options=enumerate(ssids))
                    # while wifi_SSID == "":
                    #     # start input searching, on input rotate ssids and then reshow the image
                    #     # when hit select, set wifiSSID to be the first element in the list
                    #     pass
                    # self.changeWifi(wifi_SSID, wifi_PASS)
                    # didWifiConnect = self.connectToWiFi()
            if globalvars.buttons["RT"].is_pressed: # NO
                usingWifi = False
        globalvars.wifiModeActive = usingWifi
                
        
        
    def changeWifi(self, name, password):
        # Read the current wpa_supplicant.conf file
        config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
        
        # Create a temporary file to store the modified configuration
        temp_file = f'/tmp/{os.getpid()}_wpa_supplicant.conf'
        
        try:
            # Read the existing configuration
            with open(config_file, 'r') as f:
                content = f.read()
            
            # Parse the content to find the last network block
            lines = content.split('\n')
            last_network_index = None
            for i, line in enumerate(lines):
                if line.startswith('network={'):
                    last_network_index = i
                    break
            
            # Add the new network block after the last existing one
            if last_network_index is not None:
                lines.insert(last_network_index + 1, '\n')
                lines.insert(last_network_index + 2, f'network={{\n')
                lines.insert(last_network_index + 3, f'    ssid="{name}"\n')
                lines.insert(last_network_index + 4, f'    psk="{password}"\n')
                lines.insert(last_network_index + 5, '}}\n')
            
            # Write the modified content to the temporary file
            with open(temp_file, 'w') as f:
                f.writelines(lines)
            
            # Replace the original file with the modified version
            os.replace(temp_file, config_file)
            
            # Reload the Wi-Fi configuration
            os.system('sudo wpa_cli -i wlan0 reconfigure')
            
            print(f"Successfully updated Wi-Fi connection to {name}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def connectToWiFi(self):
        # Wait for the network interface to be ready
        time.sleep(10)

        # Get the current IP address
        result = subprocess.run(['hostname', '-I'])
        ip_address = result.stdout.decode().strip()

        if ip_address:
            print(f"Connected to Wi-Fi. Current IP: {ip_address}")
            return True
        else:
            print("Failed to connect to Wi-Fi. Attempting to update Wi-Fi settings.")
            return False
        
    def registerApps(self):
        
        count = 0
        for file_name in os.listdir("apps"):
            if file_name.endswith(".py"):
                class_name = file_name[:-3]  # Remove the .py extension
                classToRegister = getattr(__import__('apps.' + class_name, globals(), locals(), [class_name], 0), class_name)
                
                instance = classToRegister()
                count = count + 1
                
