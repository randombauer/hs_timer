import PIL.ImageGrab
from __future__ import print_function
import pygtk
import gtk, gobject
import time
import datetime
import os

x = 1234
y = 394
start = datetime.now()
own_turn_counter = 90
own_overall_counter = 0
enemy_turn_counter = 90
enemy_overall_counter = 0
overall_gametime = 0
yellow = (255, 255, 46)
green = (89, 252, 45)

def get_pixel_colour(i_x, i_y):
	return PIL.ImageGrab.grab().load()[i_x, i_y]
  
def check_colour():
	colour = get_pixel_colour(x, y)
	if colour == yellow or colour == green: 
		return 1
	else:
		return 0
		
def reset_turn_counter(counter):
	return 90

class Timer:

    def destroy(self, widget, data=None):
        print ("Destroy event!")
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Hearthstone Timer!")
        window.set_size_request(400, 600)
        self.window = window
        self.counter = 1

        self.IsPaused = False
        self.NextButton = gtk.Button("Next")
        self.PauseButton = gtk.Button("Pause")
        self.StartButton = gtk.Button("Start")
        self.NextButton.connect("clicked", self.LapTimer) # Next Split
        self.PauseButton.connect("clicked", self.PauseTimer) # Pause
        self.StartButton.connect("clicked", self.StartTimer) # Start

        self.RunTimer = None
        self.NewTime = None
        self.TheSplits = []
        self.LapList = []
        self.TheTimes = []
        self.AllSplits = []
        self.TimeBar = gtk.Statusbar()
        self.TimeBar.push(1, "0.00")

        hbox = gtk.HBox()
        NextBox = gtk.VBox()
        PauseBox = gtk.VBox()
        StartBox = gtk.VBox()
        NextBox.pack_end(self.NextButton, expand=True, fill=False, padding=20)
        PauseBox.pack_end(self.PauseButton, expand=True, fill=False, padding=20)
        StartBox.pack_end(self.StartButton, expand=True, fill=False, padding=0)
        hbox.pack_end(NextBox, expand=True, fill=False, padding=0)
        hbox.pack_end(PauseBox, expand=True, fill=False, padding=0)
        hbox.pack_end(StartBox, expand=True, fill=False, padding=0)

        vbox = gtk.VBox()
        TimeBox = []
        self.AddSplits(TimeBox)
        for b in range(0, len(TimeBox)):
            vbox.pack_start(TimeBox[b], expand=True, fill=True, padding=0)
        vbox.pack_end(hbox, expand=False, fill=True, padding=0)
        vbox.pack_end(self.TimeBar, expand=True, fill=True, padding=20)

        self.window.add(vbox)
        self.window.connect("destroy", self.destroy)

        self.window.show_all()

    def ReadTimes(self):
        if os.path.isfile('Runs'+self.AllSplits[0]):
            Old = open('Runs'+self.AllSplits[0], 'r')
            self.OldRuns = Old.readlines()
            for s in range (1,len(self.OldRuns)):
                self.TheTimes[s-2].set_text(self.OldRuns[s])
 #       else:
#            self.TheTimes[1].set_text("0.00")

    def AddSplits(self, TimeBox):
        with open('MySplits', 'r') as SplitData:
            self.AllSplits = SplitData.readlines()
        self.AllSplits[0] = self.AllSplits[0][:-1]
        self.TheSplits.append(gtk.Label())
        self.TheSplits[0].set_text(self.AllSplits[0])
        TimeBox.append(gtk.HBox())
        TimeBox[0].pack_start(self.TheSplits[0], expand=True, fill=True, padding=0)
        for x in range(1, len(self.AllSplits)):
            self.AllSplits[x] = self.AllSplits[x][:-1]
            self.TheSplits.append(gtk.Label())
            self.TheTimes.append(gtk.Label())
            self.TheSplits[x].set_text(self.AllSplits[x])
            self.ReadTimes()

            TimeBox.append(gtk.HBox())
            TimeBox[x].pack_start(self.TheSplits[x], expand=False, fill=True, padding=0)
            TimeBox[x].pack_start(self.TheTimes[x-1], expand=False, fill=True, padding=10)



    def UpdateTimer(self):
        self.NewTime = time.time() - self.OldTime
        self.ActualTime = str(datetime.timedelta(seconds=self.NewTime))
        self.TheTimes[(self.counter-1)].set_text("%s" % self.ActualTime)
        self.TimeBar.push(1, "%s" % self.ActualTime)
        return True

    def StartTimer(self, StartButton):
        self.OldTime = time.time()
        self.RunTimer = gobject.timeout_add(10, splits.UpdateTimer)

    def InsertTimes(self):
        pass

    def PauseTimer(self, PauseButton):
        if self.IsPaused == False:
            gobject.source_remove(self.RunTimer)
            print ("Stopped")
            self.IsPaused = True
        else:
            self.OldTime = time.time() - self.NewTime
            self.RunTimer = gobject.timeout_add(10, splits.UpdateTimer)
            print ("Resumed")
            self.IsPaused = False

    def LapTimer(self, NextButton):
        self.LapList.append(self.NewTime)
        self.counter = self.counter + 1
        if self.counter >= len(self.TheSplits):
            gobject.source_remove(self.RunTimer)
            f = open(('Runs'+self.AllSplits[0]), 'a')
            f.write('Runs:\n')
            for a in self.LapList:
                f.write("%s\n" %a)
            print ("All Splits done")

    def main(self):
        self.RunTimer
        gtk.main()


if __name__ == "__main__":
    splits = Splits()
    splits.main()

	


	

	
