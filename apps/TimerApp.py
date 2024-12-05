from AppAPI import *
from globalvars import *
import urequests as requests
from time import sleep
from machine import Timer

class TimerApp:
    
    def __init__(self):
        self.timerIsRunning = False
        self.timeDigitSetting = False
        self.timerCurrentHours = 0
        self.timerCurrentMins = 0
        self.timerCurrentSecs = 0
        self.timerHours = 0
        self.timerMins = 0
        self.timerSecs = 0
        self.timer = None
        TimerApp = App("timer", "Timer")
        #TimerApp.setAppDefinedCommands(
            #setStartCheckTimer={"name": "Set/Start/Check", "method":self.set_start_check},
            #pauseStopTimer={"name": "Pause/Stop", "method":self.pause_stop}
            #)
    
    def set_start_check(self):
        if timerIsRunning:
            if timeDigitSetting == 5:
                # start timer
                pass
            else:
                # move digit being editied
                pass
        else:
            # Check Time
            pass
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
