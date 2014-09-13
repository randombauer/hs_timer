#!/usr/bin/python

from __future__ import print_function
import pygtk
import gtk, gobject
import os
from timer import *
from colour import *


class Window:

    def destroy(self, widget, data=None):
        print ("Destroy event!")
        gtk.main_quit()
        
    def __init__(self, StartTime):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Hearthstone Timer!")
        window.set_size_request(400, 600)

        self.own_timer = Timer()
        self.colour_checker = Colour()
        self.window = window
        self.counter = 1

        self.StopButton = gtk.Button("Stop")
        self.PauseButton = gtk.Button("Pause")
        self.StartButton = gtk.Button("Start")
        self.StopButton.connect("clicked", self.Stop) # Stop
        self.PauseButton.connect("clicked", self.Pause) # Pause
        self.StartButton.connect("clicked", self.Start) # Start

        self.Run = None
        self.Up = None
        self.StartTime = str(datetime.timedelta(seconds=StartTime))
        self.TimeBar = gtk.Statusbar()
        self.TimeBar.push(1, "%s" % self.StartTime)

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

    def Update(self):
        self.Up = self.own_timer.UpdateTimer()
        self.TimeBar.push(1, "%s" % self.Up)
        return True

    def Start(self):
        self.own_timer.StartTimer()
        self.Run = gobject.timeout_add(10, self.Update)

    def Pause(self):
        self.own_timer.PauseTimer(self.Run)

    def Stop(self):
        self.own_timer.StopTimer(self.Run)

    def Reset(self):
        self.TimeBar.push(1, "%s" % self.StartTime)

    def Start_with_button(self, StartButton):
        self.own_timer.StartTimer()
        self.Run = gobject.timeout_add(10, self.Update)

    def Pause_with_button(self, PauseButton):
        if PauseButton.get_label() == "Pause":
            PauseButton.set_label("Resume")
            self.own_timer.PauseTimer(self.Run)
        else:
            PauseButton.set_label("Pause")
            self.Run = gobject.timeout_add(10, self.Update)

    def Stop_with_button(self, StopButton):
        if StopButton.get_label() == "Stop":
            self.own_timer.StopTimer(self.Run)
            StopButton.set_label("Reset")
        else:
            self.TimeBar.push(1, "%s" % self.StartTime)
            StopButton.set_label("Stop")

    def main(self):
        self.Run
        gtk.main()


if __name__ == "__main__":
    window = Window(90)
    window.main()
