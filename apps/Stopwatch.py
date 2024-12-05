from AppAPI import *
from globalvars import *
import urequests as requests
from time import sleep
from machine import Timer

class Stopwatch:
    
    def __init__(self):
        self.stopwatchIsRunning = False
        self.stopwatchHours = 0
        self.stopwatchMins = 0
        self.stopwatchSecs = 0
        self.stopwatch = None
        StopwatchApp = App("stopwatch", "Stopwatch")
        StopwatchApp.setAppDefinedCommands(
            startCheckStopwatch={"name": "Start/Check", "method":self.start_check},
            pauseStopStopwatch={"name": "Pause/Stop", "method":self.pause_stop}
            )
    
    def start_check(self):
        if self.stopwatchIsRunning:
            if self.stopwatch == None:
                return
            screen.clear()
            screen.move_to(0,0)
            screen.putstr("Stopwatch")
            screen.move_to(0,1)
            screen.putstr(f"{self.stopwatchHours:02}:{self.stopwatchMins:02}:{self.stopwatchSecs:02}")
            sleep(1)
            screen.clear()
        else:
            screen.clear()
            screen.move_to(0,0)
            screen.putstr("Stopwatch")
            screen.move_to(0,1)
            screen.putstr("Starting")
            self.stopwatch = Timer(period=1000, callback=self.increment_time)
            self.stopwatchIsRunning = True
            sleep(1)
            screen.clear()
    def pause_stop(self):
            self.stopwatch.deinit()
            if self.stopwatchIsRunning:
                screen.clear()
                screen.move_to(0,0)
                screen.putstr("Stopwatch")
                screen.move_to(0,1)
                screen.putstr("Paused")
                self.stopwatchIsRunning=False
                sleep(1)
                screen.clear()
            else:
                screen.clear()
                screen.move_to(0,0)
                screen.putstr("Stopwatch")
                screen.move_to(0,1)
                screen.putstr("Cleared")
                self.stopwatchSecs = 0
                self.stopwatchMins = 0
                self.stopwatchHours = 0
                sleep(1)
                screen.clear()

    def increment_time(self, Timer):
        self.stopwatchSecs += 1
        if self.stopwatchSecs == 60:
            self.stopwatchSecs = 0
            self.stopwatchMins += 1
            if self.stopwatchMins == 60:
                self.stopwatchMins = 0
                self.stopwatchHours += 1
                if self.stopwatchHours == 100:
                    self.stopwatchHours = 0