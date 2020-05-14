from sense_hat import SenseHat
from gpiozero import CPUTemperature

sense = SenseHat()

white = (255,255,255)
off = (0, 0, 0)

sense.low_light = True
sense.set_rotation(270)
def printHumidity():
    sense.clear()
    h = sense.get_humidity()
    h = round(h, 1)

    sense.show_message("Humidity: " + str(h) + "%", text_colour=white, back_colour=off, scroll_speed=0.08)
    sense.clear()

def printTemp():
    sense.clear()
    t = sense.get_temperature()
    t = (t * 9/5 ) + 32
    t = round(t, 1)

    sense.show_message("Temp: " + str(t) + " deg. F", text_colour=white, back_colour=off, scroll_speed=0.08)
    sense.clear()
    
def printBaro():
    sense.clear()
    p = sense.get_pressure()
    p = p / 33.864
    p = round(p, 1)

    sense.show_message("Baro: " + str(p) + " inHg", text_colour=white, back_colour=off, scroll_speed=0.08)
    sense.clear()

def printCPUTemp():
    for i in range(1):
        sense.clear()
        ct = CPUTemperature().temperature
        ct = round(ct, 1)

        sense.show_message("CPU: " + str(ct) + " deg. C", text_colour=white, back_colour=off, scroll_speed=0.08)
        sense.clear()

    
sense.stick.direction_up = printHumidity
sense.stick.direction_left = printTemp
sense.stick.direction_right = printBaro
sense.stick.direction_down = printCPUTemp



