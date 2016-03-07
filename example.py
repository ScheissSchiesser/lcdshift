#!/usr/bin/env python
import lcdshift
from datetime import datetime
seemeshift = lcdshift.lcdshift()
x=0
while x<10:
    d = datetime.now().strftime("%A, %B %e, %Y")
    t = datetime.now().strftime("%I:%M:%S %p")
    seemeshift.scrollOneLine(d + " " + t)
    x=x+1
