#!/usr/bin/python

import gtk

class Colour:

    def __init__(self):
        self.x = 1234
        self.y = 394
        self.yellow = (255, 255, 46)
        self.green = (89, 252, 45)

    def get_pixel_colour(self):
        buff = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
        buff.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), self.x, self.y, 0, 0, 1, 1)
        return tuple(buff.get_pixels_array().tolist()[0][0])
 
    def check_colour(self):
        colour = get_pixel_colour(x, y)
        if colour == yellow or colour == green:
            return 1
        else:
            return 0

    def main(self):
        print self.get_pixel_colour()

if __name__ == "__main__":
    colour = Colour()
    colour.main()
