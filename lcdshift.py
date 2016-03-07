#!/usr/bin/env python
from wiringpi2 import *
from datetime import datetime
from time import sleep
wiringPiSetup() #use wiringPi pin scheme

#assign values to 595's pins
pinBase = 100
RS =  pinBase + 0
E =   RS + 1
DB4 = E + 1
DB5 = DB4 + 1
DB6 = DB5 + 1
DB7 = DB6 + 1
cols = 16
rows = 2

#Pi's pin out using WiringPi's scheme
dataPin, clockPin, latchPin = 23, 25, 24

#           pin @ QA, num pins used, SER    , SRCLK   , RCLK 
sr595Setup (pinBase , 6            , dataPin, clockPin, latchPin)

def scrolling_message(text):
    # pad text with numlines.numcols - 1 blank spaces, so
    # text flies in from right
    # Do the same for trailing spaces.
    text = " "*cols + text.rstrip('\n') + " "
    
    for i in range(0, len(text)):
        lcdHome(lcd)
        lcdPuts(lcd,text[i:(i+(cols))])
        print text[i:(i+(cols))]
        sleep(0.3)

# Now, let's handle the HD44780 ...
# RS, E, DB4, DB5, DB6 and DB7's signals are coming out of the 595
lcd = lcdInit (rows, cols, 4, RS, E, DB4, DB5, DB6, DB7, 0,0,0,0)
lcdCursorBlink(lcd,False)
lcdHome(lcd)
lcdClear(lcd)
lcdPosition(lcd, 0, 0)
#lcdPuts(lcd, datetime.now().strftime("%I:%M:%S %p"))
#lcdPosition(lcd, 0, 1)
#lcdPuts(lcd, datetime.now().strftime("%A, %B %e, %Y"))

while True:
    d = datetime.now().strftime("%A, %B %e, %Y")
    t = datetime.now().strftime("%I:%M:%S %p")
    scrolling_message(d + " " + t)

lcdPosition(lcd, 0, 0)



