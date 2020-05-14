import bs4
import requests
import json
import re
from sense_hat import SenseHat
from time import sleep

#WebScrapingBitcoinTicker -- Uses text from a bitcoin tracking website
#to display the current bitcoin price to raspberry pi sense hat.


sense = SenseHat()

#Turn the LED matrix upside down

sense.set_rotation(180)

#Colors

green = (0, 255, 0)
red = (255, 0, 0)
off = (0, 0, 0)

#Don't hurt your eyes

sense.low_light = True

#Go to the website link, download all the HTML, turn it into a json file,
#scrub off script headers and footers, load into json, iterate to the price,
# return price as string.

def scrape():

    link = 'https://www.bitcoinprice.com/'
  
    page = requests.get(link)

    formated_page = bs4.BeautifulSoup(page.content, features="lxml")

    tags = formated_page.find_all('script')

    #For checking the json
    #print(str(tags[15]))

    scrubbed_string  = re.sub("<[\/]?script(.)*[>]", "" , str(tags[15]))

    group1 = json.loads(scrubbed_string)

    price_string = group1['@graph'][0]['offers']['price'] 

    return price_string

#Set prev = to 0

prev = 0


#Continuously run loop to:
    #Set temp to float of price, if float is less than prev set color to
    #red, else set to green, show message, clear message, set prev to temp
    #for next loop, wait 3 seconds.

while True:

    temp = float(scrape())
    
    if temp > prev:
        color = green
    if temp < prev:
        color = red    

    sense.show_message("$ " + str(temp), text_colour=color, back_colour=off, scroll_speed=0.05 )
    sense.clear()
    prev = temp
    #sleep(1)

sense.clear()


# For finding the element of the webpage containing prices


# counter = 1
#
# for counter in range(len(tags)):
#     print("-----" + str(counter) + "-----")
#     print(tags[counter])
#     print("\n")


