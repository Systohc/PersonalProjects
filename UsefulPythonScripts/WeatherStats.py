from sense_hat import SenseHat
from gpiozero import CPUTemperature
from time import sleep
from subprocess import run

sense = SenseHat()
sense.set_rotation(270)
for i in range(1):

    #Make green color and pixel array
    w = (0, 0, 0)
    r = (255, 0, 0)

    pixels = [
    r, r, w, w, w, w, r, r,
    r, r, r, w, w, r, r, r,
    w, r, r, w, w, r, r, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, r, r, r, r, r, r, w,
    w, w, r, r, r, r, w, w,
    w, w, w, w, w, w, w, w
    ]
   

    #Flash the screen green to notify that the script has run
    sense.set_pixels(pixels)
    sleep(0.125)
    sense.clear()

    # Use this and the sleeps if doing multiple pings
    #  run("clear")

    # sleep(0.25)

    cpu_temp = CPUTemperature().temperature

    t = sense.get_temperature()
    h = sense.get_humidity()
    p = sense.get_pressure()

    # Convert to imperial units

    #Uncomment to have cpu temp in F but also change string
    cpu_tempF = (cpu_temp * 9/5) + 32
    t = (t * 9/5) + 32
    p = p / 33.864

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    cpu_temp = round(cpu_temp, 1)
    cpu_tempF = round(cpu_tempF, 1)

    # Assemble String
    message = ("The Ambient Temperature is: " + str(t) + " degrees F, however this is being\neffected by W.O.R.M.'s CPU which is currently: " +
        str(cpu_temp) + " degrees C, " + str(cpu_tempF) + " degrees F." + "\n\nThe Humidity is: "
        + str(h) + "%" + "\n\nThe Barometric Pressure is: " + str(p) + " inHg\n\nW.O.R.M. can sense many things about his surroundings...")

    # Uncomment one of these depending on whether
    # or not it will be run in python, or command line

    run(["echo", message])

    #print(message)

   # sleep(0.25)

    
