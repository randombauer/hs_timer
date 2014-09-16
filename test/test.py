#!/usr/bin/python

from __future__ import print_function
import pygtk
import gtk, gobject
import os

class Test:

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        test = gtk.Window(gtk.WINDOW_TOPLEVEL)
        test.set_title("Colour changer")
        test.set_size_request(200, 200)

        self.test = test

        self.GreenButton = gtk.Button("Green")
        self.YellowButton = gtk.Button("Yellow")
        self.GreyButton = gtk.Button("Grey")
        self.GreenButton.connect("clicked", self.go_green) # Green background
        self.YellowButton.connect("clicked", self.go_yellow) # Yellow background
        self.GreyButton.connect("clicked", self.go_grey) # Gre3y background

        hbox = gtk.HBox()
        hbox2 = gtk.HBox()
        self.eb = gtk.EventBox()
        self.eb.add(hbox2)
        GreenBox = gtk.VBox()
        YellowBox = gtk.VBox()
        GreyBox = gtk.VBox()

        GreenBox.pack_end(self.GreenButton, expand=True, fill=False, padding=20)
        YellowBox.pack_end(self.YellowButton, expand=True, fill=False, padding=20)
        GreyBox.pack_end(self.GreyButton, expand=True, fill=False, padding=0)
        hbox.pack_end(GreenBox, expand=True, fill=False, padding=0)
        hbox.pack_end(YellowBox, expand=True, fill=False, padding=0)
        hbox.pack_end(GreyBox, expand=True, fill=False, padding=0)

        vbox = gtk.VBox()
        vbox.pack_end(hbox, expand=False, fill=True, padding=0)
        vbox.pack_end(self.eb, expand=True, fill=True, padding=20)

        self.test.add(vbox)
        self.test.connect("destroy", self.destroy)

        self.test.show_all()

    
    def go_yellow(self, YellowButton):
        self.eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(red=45000, green=45000, blue=3000))

    def go_green(self, GreenButton):
        self.eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(red=28000, green=45000, blue=12500))

    def go_grey(self, GreyButton):
        self.eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(red=32000, green=32000, blue=32000))

    def main(self):
        gtk.main()

if __name__ == "__main__":
    test = Test()
    test.main()
