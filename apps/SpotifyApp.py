from AppAPI import *
from globalvars import *
import urequests as requests
from time import sleep

class SpotifyApp:
        
    def play_pause(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/playpause')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    def shuffle_toggle(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/shuffletoggle')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    def repeat_toggle(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/repeattoggle')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    def skip(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/next')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    def previous(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/back')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    def volume_up(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/volume/up')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    def volume_down(self):
        response = requests.get('https://gloveserver.heckerwithahat.dev/spotify/volume/down')
        screen.clear()
        screen.move_to(0,0)
        screen.putstr("Spotify")
        screen.move_to(0,1)
        screen.putstr(response.text)
        sleep(1)
        screen.clear()
        
    
    def __init__(self):
        SpotifyApp = App("spotify", "Spotify")
        SpotifyApp.setAppDefinedCommands(
            playpause={"name": "Play/Pause", "method":self.play_pause},
            shuffletoggle={"name": "Shuffle", "method":self.shuffle_toggle},
            repeattoggle={"name": "Repeat", "method":self.repeat_toggle},
            skipsong={"name": "Skip", "method":self.skip},
            previoussong={"name": "Back", "method":self.previous},
            volumeup={"name": "Volume Up", "method":self.volume_up},
            volumedown={"name": "Volume Down", "method":self.volume_down}
            )
        
        

    

