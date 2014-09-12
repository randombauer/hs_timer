#!/usr/bin/python

from __future__ import print_function
import pygtk
import gtk, gobject
import time
import datetime
import os

class Stopwatch:

    def destroy(self, widget, data=None):
        print ("Destroy event!")
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Hearthstone Stopwatch!")
        window.set_size_request(400, 600)
        self.window = window
        self.counter = 1



        self.IsPaused = False
        self.StopButton = gtk.Button("Stop")
        self.PauseButton = gtk.Button("Pause")
        self.StartButton = gtk.Button("Start")
        self.StopButton.connect("clicked", self.StopStopwatch) # Stop
        self.PauseButton.connect("clicked", self.PauseStopwatch) # Pause
        self.StartButton.connect("clicked", self.StartStopwatch) # Start

        self.RunStopwatch = None
        self.NewTime = None
        self.TimeBar = gtk.Statusbar()
        self.TimeBar.push(1, "0.00")

        hbox = gtk.HBox()
        PauseBox = gtk.VBox()
        StartBox = gtk.VBox()
        StopBox = gtk.VBox()
        StopBox.pack_end(self.StopButton, expand=True, fill=False, padding=20)
        PauseBox.pack_end(self.PauseButton, expand=True, fill=False, padding=20)
        StartBox.pack_end(self.StartButton, expand=True, fill=False, padding=0)
        hbox.pack_end(StopBox, expand=True, fill=False, padding=0)
        hbox.pack_end(PauseBox, expand=True, fill=False, padding=0)
        hbox.pack_end(StartBox, expand=True, fill=False, padding=0)

        vbox = gtk.VBox()
        TimeBox = []
        for b in range(0, len(TimeBox)):
            vbox.pack_start(TimeBox[b], expand=True, fill=True, padding=0)
        vbox.pack_end(hbox, expand=False, fill=True, padding=0)
        vbox.pack_end(self.TimeBar, expand=True, fill=True, padding=20)

        self.window.add(vbox)
        self.window.connect("destroy", self.destroy)

        self.window.show_all()

    def UpdateStopwatch(self):
        self.NewTime = time.time() - self.OldTime
        self.ActualTime = str(datetime.timedelta(seconds=self.NewTime))
        self.TimeBar.push(1, "%s" % self.ActualTime)
        return True

    def StartStopwatch(self, StartButton):
        self.OldTime = time.time()
        self.RunStopwatch = gobject.timeout_add(10, stopwatch.UpdateStopwatch)

    def PauseStopwatch(self, PauseButton):
        if self.IsPaused == False:
            PauseButton.set_label("Resume")
            gobject.source_remove(self.RunStopwatch)
            print ("Stopped")
            self.IsPaused = True
        else:
            PauseButton.set_label("Pause")
            self.OldTime = time.time() - self.NewTime
            self.RunStopwatch = gobject.timeout_add(10, stopwatch.UpdateStopwatch)
            print ("Resumed")
            self.IsPaused = False

    def StopStopwatch(self, StopButton):
        gobject.source_remove(self.RunStopwatch)
        StopButton.set_label("Reset")
    #FIXME
    #    if StopButton.clicked():
    #        self.OldTime = time.time()
    #        StopButton.set_label("Stop")

    def main(self):
        self.RunStopwatch
        gtk.main()


if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.main()
