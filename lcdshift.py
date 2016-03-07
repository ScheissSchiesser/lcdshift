#!/usr/bin/env python
from wiringpi2 import *
from time import sleep
wiringPiSetupGpio() #use wiringPi pin scheme

class lcdshift:
    def __init__(self,cols=16,rows=2,dataPin=13,clockPin=26,latchPin=19):
        self.cols = cols
        self.rows = rows
        #assign values to 595's pins
        #Pi's pin out using WiringPi's scheme
        pinBase = 100
        RS =  pinBase + 0
        E =   RS + 1
        DB4 = E + 1
        DB5 = DB4 + 1
        DB6 = DB5 + 1
        DB7 = DB6 + 1
        #          pin @ QA, num pins used, DS, SRCLK, RCLK 
        sr595Setup(pinBase, 6, dataPin, clockPin, latchPin)
        # Now, let's handle the HD44780 ...
        # RS, E, DB4, DB5, DB6 and DB7's signals are coming out of the 595
        self.lcd = lcdInit(rows, cols, 4, RS, E, DB4, DB5, DB6, DB7, 0,0,0,0)
        lcdClear(self.lcd)
        lcdCursorBlink(self.lcd,False)
        
    def scrollOneLine(self,text,countby=5,delay=0.15,flyin=False,repeat=False):
        cols = self.cols
        lcd = self.lcd

        if flyin:
            # pad text with cols - 1 blank spaces, so
            # text flies in from right
            startpad = cols
        else:
            startpad = 0
        # Remove newline characters to display only on one line
        text_nonewline = text.rstrip('\n')
        textpad = " "*startpad + text_nonewline + " " + text_nonewline[0:cols]
        endPadLength = (len(textpad)-cols) % countby
        textpad = textpad + " "*endPadLength
        # loop through the text
        for i in range(0, len(textpad)-cols+1,countby):
            lcdPosition(lcd, 0, 0)        
            lcdPuts(lcd,textpad[i:(i+(cols))])
            print textpad[i:(i+(cols))]
            sleep(delay*countby)

    def autoscroll(self,text):
        try:
            pass
        except:
            pass

