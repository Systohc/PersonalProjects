from sense_hat import SenseHat

sense = SenseHat()

sense.low_light = True
sense.set_rotation(270)

green = (0, 100, 0)

def sayHello():
    sense.show_message("Hello Koith, I am the brain of W.O.R.M, the Wriggling Organic Ruckus Maker.",
                       text_colour=green, scroll_speed=0.1)

sense.stick.direction_middle = sayHello
