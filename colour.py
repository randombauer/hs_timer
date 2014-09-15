#!/usr/bin/python

from PIL import *
import gtk
import Image
import sys
import os

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
        if sys.argv[1] == "test":
            print "=== Fixed RGB Ranges - Test Started ==="
            for img in sorted(os.listdir('img/')):
                im = Image.open("img/"+img)
                pix = im.convert("RGB")
                r,g,b = pix.getpixel((1046, 336))

                if 35 < r < 180 and 150 < g < 255 and 0 < b < 175:
                    print ("%s: (%s, %s, %s) ==> Green" % (img, r, g, b))
                elif 100 < r < 255 and 120 < g < 255 and 0 < b < 60:
                    print ("%s: (%s, %s, %s) ==> Yellow" % (img, r, g, b))
                else:
                    print ("%s: (%s, %s, %s) ==> Grey or different Color" % (img, r, g, b))

            print "=== Fixed RGB Ranges - Test finished ==="
            print "========================================"
            print "=== Average RGB Value - Test Started ==="
            self.average_image_color()
            print "=== Average RGB Value - Test finished ==="
            sys.exit(0)

        else:
            buff = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
            buff.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), self.x, self.y, 0, 0, 1, 1)
            return tuple(buff.get_pixels_array().tolist()[0][0])

    def check_colour(self):
        colour = self.get_pixel_colour()
        if colour == self.yellow or colour == self.green:
            return 1
        else:
            return 0

    def average_image_color(self):
        for img in sorted(os.listdir('img/')):
            im = Image.open("img/"+img)
            box = (975,296,1090,355)
            crop = im.crop(box)
            h = crop.histogram()
            #crop.show()

        # split into red, green, blue
            r = h[0:256]
            g = h[256:256*2]
            b = h[256*2: 256*3]

        # perform the weighted average of each channel:
        # the *index* is the channel value, and the *value* is its weight
            print (
                sum( i*w for i, w in enumerate(r) ) / sum(r),
                sum( i*w for i, w in enumerate(g) ) / sum(g),
                sum( i*w for i, w in enumerate(b) ) / sum(b)
            )
        return 1

    def test(self):
        if self.check_colour():
            print "Success"
        else:
            print "Eher nicht, nein"

    def main(self):
        self.test()
        print self.get_pixel_colour()

if __name__ == "__main__":
    colour = Colour()
    colour.main()
