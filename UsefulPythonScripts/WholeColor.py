from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (0, 0, 0)
r = (180, 0, 0)

def evil():
    sense.clear()
    pixels = [
        r, r, w, w, w, w, r, r,
        r, r, r, w, w, r, r, r,
        w, r, r, w, w, r, r, w,
        w, w, w, w, w, w, w, w,
        r, r, w, w, w, w, r, r,
        w, r, r, r, r, r, r, w,
        w, w, r, r, r, r, w, w,
        w, w, w, w, w, w, w, w
    
    ]

    sense.set_pixels(pixels)

def good():
    sense.clear()
    pixels = [
        w, w, w, w, w, w, w, w,
        w, r, r, w, w, r, r, w,
        w, r, r, w, w, r, r, w,
        w, w, w, w, w, w, w, w,
        w, w, w, w, w, w, w, w,
        w, r, r, r, r, r, r, w,
        w, w, r, r, r, r, w, w,
        w, w, w, w, w, w, w, w
    
    ]

    sense.set_pixels(pixels)

def clear():
    sense.clear()

sense.stick.direction_up = good
sense.stick.direction_down = evil
sense.stick.direction_right = clear

while True:
    pass
