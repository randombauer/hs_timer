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

        # Init buttons
        # Buttons are not really needed for the timer but at the moment they
        # allow for easy testing and control
        self.StartButton = gtk.Button("Start")
        self.StartButton.connect("clicked", self.Start_with_button) # Start

        self.Run = None
        self.Up = None
        self.Turn_status = None
        self.Old_status = None
        self.StartTime = str(datetime.timedelta(seconds=StartTime))
        self.TimeBar = gtk.Statusbar()
        self.TimeBar.push(1, "%s" % self.StartTime)

        hbox = gtk.HBox()
        StartBox = gtk.VBox()
        StartBox.pack_end(self.StartButton, expand=True, fill=False, padding=0)
        hbox.pack_end(StartBox, expand=True, fill=False, padding=0)

        vbox = gtk.VBox()
        vbox.pack_end(hbox, expand=False, fill=True, padding=0)
        vbox.pack_end(self.TimeBar, expand=True, fill=True, padding=20)

        self.window.add(vbox)
        self.window.connect("destroy", self.destroy)

        self.window.show_all()

    def Update(self):
        self.check_turn_status()
        # Restart the timer when it's our turn again
        if self.Turn_status == True and self.Old_status == False:
            self.own_timer.StartTimer()
        if self.Turn_status == True:
            self.Up = self.own_timer.UpdateTimer()
            print (self.Run)
            self.TimeBar.push(1, "%s" % self.Up)
            self.Old_status = self.Turn_status
            return True
        else:
            self.TimeBar.push(1, "%s" % self.StartTime)
            self.Old_status = self.Turn_status
            return True

    def check_turn_status(self):
        self.Turn_status = self.colour_checker.check_colour()

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

    def main(self):
        self.Run
        gtk.main()


if __name__ == "__main__":
    window = Window(90)
    window.main()
