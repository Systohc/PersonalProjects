from sense_hat import SenseHat
from time import sleep
from gpiozero import CPUTemperature

sense = SenseHat()

sense.clear()

cpu_temp = 0
previous_cpu_temp = 0

color = (0, 255, 0)

pixel_color = []

seconds = 0
minutes = 0

for i in range(64):
    pixel_color.append(color)

while cpu_temp < 60:
    cpu_temp = CPUTemperature().temperature

    cpu_temp = round(cpu_temp, 1)
    
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    else:
        seconds = seconds + 1

    if cpu_temp != previous_cpu_temp:    
        print(str(cpu_temp) + " C")
        previous_cpu_temp = cpu_temp

    sleep(1)
    
print("Time it took to overheat: " + str(minutes) + "m " + str(seconds) + "s")

while True:
    sleep(1)
    sense.set_pixels(pixel_color)
    sleep(0.125)
    sense.clear()
    sleep(0.125)
    sense.set_pixels(pixel_color)
    sleep(0.125)
    sense.clear()
