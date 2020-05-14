from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

w = (0, 0, 0)
r = (255, 0, 0)

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
sleep(5)


sense.clear()
