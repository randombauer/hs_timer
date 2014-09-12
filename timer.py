#!/usr/bin/python

from __future__ import print_function
import pygtk
import gtk, gobject
import time
import datetime
import os

class Timer:

    def destroy(self, widget, data=None):
        print ("Destroy event!")
        gtk.main_quit()

    def __init__(self):
        self.RunTimer = None
        self.NewTime = None
        self.IsPaused = False

    def UpdateTimer(self):
        self.NewTime = time.time() - self.OldTime
        self.NewTime = 90 - self.NewTime
        self.ActualTime = str(datetime.timedelta(seconds=self.NewTime))
        return self.ActualTime

    def StartTimer(self):
        self.OldTime = time.time()

    def PauseTimer(self, PauseButton):
        if self.IsPaused == False:
            PauseButton.set_label("Resume")
            gobject.source_remove(self.RunTimer)
            print ("Stopped")
            self.IsPaused = True
        else:
            PauseButton.set_label("Pause")
            self.OldTime = time.time() - self.NewTime
            self.RunTimer = gobject.timeout_add(1000, timer.UpdateTimer)
            print ("Resumed")
            self.IsPaused = False

    def StopTimer(self, StopButton):
        gobject.source_remove(self.RunTimer)
        StopButton.set_label("Reset")
    #FIXME
    #    if StopButton.clicked():
    #        self.OldTime = time.time()
    #        StopButton.set_label("Stop")

    def main(self):
        self.RunTimer

class CountDownTimer(Timer):

    def UpdateTimer(self):
        self.NewTime = 90 - (time.time() - self.OldTime)
        self.ActualTime = str(datetime.timedelta(seconds=self.NewTime))
        self.TimeBar.push(1, "%s" % self.ActualTime)
        return True


if __name__ == "__main__":
    timer = CountDownTimer()
    timer.main()
