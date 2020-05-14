
# Testing scripting on python with raspberry pi

from sense_hat import SenseHat

sense = SenseHat()

blue = (0, 0, 255)

yellow = (255, 255, 0)

for i in range(2):
  sense.show_message("Idk... seems pretty gay.", text_colour=yellow, back_colour=blue, scroll_speed=0.05)


sense.clear()
# run(['echo', 'hellothar'])

 # print("hello mate")




