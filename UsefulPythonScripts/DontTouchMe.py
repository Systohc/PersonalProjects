from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
off = (0, 0, 0)

sense.clear()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    if x > 1 or y > 1 or z > 1:
        print("Pi Has Been Disturbed")
        for i in range(3):
            sleep(0.25)
            sense.show_letter("!", red)
            sleep(0.25)
            sense.clear()

        sleep(1)   
        sense.show_message("Don't Touch Me", text_colour=red, back_colour=off, scroll_speed=0.05)
        sense.clear()
        


