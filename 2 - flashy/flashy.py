#!/usr/bin/env python3

#
# Learning about the LEDs on the EV3 Brick
# Introduces lists and loops.
#

import os
import time

from ev3dev2.led import Leds

# An LED is a type of light. That's what lights up the front of the EV3 brick.
# And you can change their colour

# First up, we need to create an instance of the Leds class...
leds = Leds()

# Guess what we're doing here...
leds.set_color("RIGHT", "RED")

# This is a list of all the colours that the LEDs can be:
colours = ['BLACK', 'RED', 'GREEN', 'AMBER', 'ORANGE', 'YELLOW'] 

# And what if we wanted to use all the colours in the list?
for colour in colours:
    # each value in the list is copied into colour (one at a time)
    print(colour) # <-- What do you think this does?
    leds.set_color("LEFT", colour)
    leds.set_color("RIGHT", colour)
    time.sleep(2)

#
# Can you change the colours to make the lights operate in the same pattern
# as a traffic light? eg GREEN -> AMBER (ORANGE) -> RED -> GREEN -> AMBER (ORANGE) -> RED
#
