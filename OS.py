import subprocess
import os
import time


# TODO:
# ADD A UPDATE BUTTONS METHOD


class OS:
    def __init__(self, wifi_SSID, wifi_PASS):
        # Boot up the OS
        # Ask for if the user wants to start in wifi mode
        # If yes do all the wifi stuff, and set the wifi variable in global vars to true
        # If no, just boot up the OS, and set the wifi variable in global vars to false
        didWifiConnect = self.connectToWiFi()
        while didWifiConnect == False:
            self.changeWifi(wifi_SSID, wifi_PASS)
            didWifiConnect = self.connectToWiFi()
        
        
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
        screen.move_to(0, 1)
        screen.putstr("Registering Apps")
        sleep(1)
        count = 0
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Glove OS Booting")
        screen.move_to(0, 1)
        screen.putstr(str(count) + " Registered")
        for file_name in os.listdir("apps"):
            if file_name.endswith(".py"):
                class_name = file_name[:-3]  # Remove the .py extension
                classToRegister = getattr(__import__('apps.' + class_name, globals(), locals(), [class_name], 0), class_name)
                
                instance = classToRegister()
                count = count + 1
                screen.move_to(0, 1)
                screen.putstr(str(count) + " Registered")
