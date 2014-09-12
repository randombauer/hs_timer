import PIL.ImageGrab

x = 1234
y = 394
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
