#!/usr/bin/python

from __future__ import print_function
import pygtk
import gtk, gobject
import time
import datetime
import os

class Timer:

    roundTime = 75

    def destroy(self, widget, data=None):
        print ("Destroy event!")
        gtk.main_quit()

    def __init__(self):
        self.RunTimer = None
        self.NewTime = None
        self.IsPaused = False

    def UpdateTimer(self):
        self.NewTime = time.time() - self.OldTime
        self.NewTime = roundTime - self.NewTime
        self.ActualTime = str(datetime.timedelta(seconds=self.NewTime))
        return self.ActualTime

    def StartTimer(self):
        self.OldTime = time.time()

    def PauseTimer(self, Run):
        if self.IsPaused == False:
            gobject.source_remove(Run)
            self.IsPaused = True
        else:
            self.OldTime = time.time() - self.NewTime
            self.IsPaused = False

    def StopTimer(self, Run):
        gobject.source_remove(Run)
		
    def main(self):
        self.RunTimer

class CountDownTimer(Timer):

    def UpdateTimer(self):
        self.NewTime = roundTime - (time.time() - self.OldTime)
        self.ActualTime = str(datetime.timedelta(seconds=self.NewTime))
        self.TimeBar.push(1, "%s" % self.ActualTime)
        return True


if __name__ == "__main__":
    timer = CountDownTimer()
    timer.main()
