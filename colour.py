#!/usr/bin/python

import gtk

class Colour:

    def __init__(self):
        self.x = 1211
        self.y = 426
        # Need to find a good way to set these values as they have a habit of
        # changing between games and sometimes even between turns (probably 
        # caused by different shadows on the button)
        self.yellow = (159, 95, 4)
        self.green = (63, 131, 6)

    def get_pixel_colour(self):
        buff = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
        buff.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), self.x, self.y, 0, 0, 1, 1)
        return tuple(buff.get_pixels_array().tolist()[0][0])
 
    def check_colour(self):
        colour = self.get_pixel_colour()
        if colour == self.yellow or colour == self.green:
            return 1
        else:
            return 0

    def test(self):
        if self.check_colour():
            print "Success"
        else:
            print "Eher nicht nein"

    def main(self):
        self.test()
#        print self.get_pixel_colour()

if __name__ == "__main__":
    colour = Colour()
    colour.main()
