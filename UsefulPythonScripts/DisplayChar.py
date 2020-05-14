from sense_hat import SenseHat

from time import sleep

sense = SenseHat()
sense.set_rotation(270)

r = (255, 0, 0)
e = (0, 0, 0)



for i in range(5):
    sleep(1)
    sense.show_letter(":", r)
    sleep(1)
    sense.clear()
