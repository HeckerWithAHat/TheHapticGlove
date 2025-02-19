from AppAPI import *
from globalvars import *
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib
import json
import socket
class SpotifyApp:

    def play_pause(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            if self.sp.current_playback()['is_playing']:
                # Pause playback
                print("Pausing music...")
                self.sp.pause_playback(device_id=active_device['id'])        
                print(f"Toggled playback on device {active_device['name']}")
                return "Paused"
            else:
                # Resume playback
                print("Resuming music...")
                self.sp.start_playback(device_id=active_device['id'])
                print(f"Toggled playback on device {active_device['name']}")
                return "Unpaused"
        except Exception as e:
            print(f"An error occurred while toggling playback: {e}")
            return "error"
        
    def shuffle_toggle(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            print(self.sp.current_playback())
            if self.sp.current_playback()['shuffle_state']:
                # Pause playback
                print("Unshuffling music...")
                self.sp.shuffle(False, device_id=active_device['id'])        
                print(f"Unshuffled playback on device {active_device['name']}")
                return "Unshuffled"
            else:
                # Resume playback
                print("Shuffling music...")
                self.sp.shuffle(True,device_id=active_device['id'])
                print(f"Shuffled playback on device {active_device['name']}")
                return "Shuffled"
        except Exception as e:
            print(f"An error occurred while toggling playback: {e}")
            return "error"
        
    def repeat_toggle(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            if self.sp.current_playback()['repeat_state'] == 'context':
                print("Not repeating music...")
                self.sp.repeat("off", device_id=active_device['id'])        
                print(f"Not repeating playback on device {active_device['name']}")
                return "Repeat Off"
            elif self.sp.current_playback()['repeat_state'] == 'track':
                print("Repeat all music...")
                self.sp.repeat("context",device_id=active_device['id'])
                print(f"Repeat all playback on device {active_device['name']}")
                return "Repeat All"
            elif self.sp.current_playback()['repeat_state'] == 'off':
                print("Repeat current music...")
                self.sp.repeat("track",device_id=active_device['id'])
                print(f"Repeat current playback on device {active_device['name']}")
                return "Repeat once"
        except Exception as e:
            print(f"An error occurred while toggling playback: {e}")
            return "error"
        
    def skip(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            self.sp.next_track(device_id=active_device['id'])
            print(f"Skipped track on device {active_device['name']}")
            return "Skipped Track"
        except Exception as e:
            print(f"An error occurred while toggling playback: {e}")
            return "error"
        
    def previous(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            self.sp.previous_track(device_id=active_device['id'])
            print(f"Back tracked on device {active_device['name']}")
            return "Back Tracked"
        except Exception as e:
            print(f"An error occurred while toggling playback: {e}")
            return "error"
        
    def volume_up(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            device_id = active_device['id']
            current_volume = active_device['volume_percent']
            self.sp.volume(device_id=device_id, volume_percent=current_volume+5)
            print(f"Decreased volume from {current_volume}% to " + str(current_volume+5) + "%")
            return "New Volume: " + str(current_volume+5)
        except Exception as e:
            print(f"Error managing volume: {e}")
            return "error"
        
    def volume_down(self):
        devices = self.sp.devices()
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if active_device is None:
            print("No active device found.")
            return "No Active Device"
        try:
            device_id = active_device['id']
            current_volume = active_device['volume_percent']
            self.sp.volume(device_id=device_id, volume_percent=current_volume-5)
            print(f"Decreased volume from {current_volume}% to " + str(current_volume-5) + "%")
            return "New Volume: " + str(current_volume-5)
        except Exception as e:
            print(f"Error managing volume: {e}")
            return "error"
        
    
    def __init__(self):
        
        self.spotify_client_id = "8f775a31bc9b4e67a8ae753400cd7cfb"
        self.spotify_client_secret = "770936463c1a47068ef59d26f1ceb143"
        self.scope='user-read-playback-state user-modify-playback-state user-read-currently-playing'
        self.redirect_uri = 'http://glove.lan:5000'
        
        # Initialize auth manager
        self.auth_manager = SpotifyOAuth(
            client_id=self.spotify_client_id,
            client_secret=self.spotify_client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope
        )
        auth_url = self.auth_manager.get_authorize_url()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 8000))
            s.listen()
            conn, addr = s.accept()
            redirect_response = f"""HTTP/1.1 302 Found
Location: {auth_url}
Content-Length: 0
Connection: close

""".encode('utf-8')
            conn.sendall(redirect_response)
            conn.close()
            s.close()
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 5000))
            s.listen()
            conn, addr = s.accept()
            print(addr)
            request = b''
            request += conn.recv(4096)
            self.code = request.decode('utf-8').split('\n')[0][11:][:-10]
            conn.close()
            s.close()
        self.auth_manager.get_access_token(code=self.code)
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
            
        
        SpotifyApp = App("spotify", "Spotify")
        SpotifyApp.setAppCommand(self.play_pause, "IT")
        SpotifyApp.setAppCommand(self.shuffle_toggle, "IM")
        SpotifyApp.setAppCommand(self.repeat_toggle, "IB")
        SpotifyApp.setAppCommand(self.skip, "MM")
        SpotifyApp.setAppCommand(self.previous, "MT")
        SpotifyApp.setAppCommand(self.volume_up, "PT")
        SpotifyApp.setAppCommand(self.volume_down, "PB")
        
        

    

