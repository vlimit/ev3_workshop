#!/usr/bin/env python3

#
# Learn about sensors and if statements
#
# Looking for API documentation for the ev3dev2 module?
#   https://media.readthedocs.org/pdf/python-ev3dev/ev3dev-stretch/python-ev3dev.pdf
#

import os
import time

from ev3dev2.sensor.lego import *
from ev3dev2.sound import Sound

# First up, we need to make an action when a sensor state has changed. How 
# about we make somes?
sound = Sound()

# We'll also be using the screen on the EV3 brick. Let's use a sensible font size.
os.system('setfont Lat15-Terminus24x12')

# 
# There are a number of sensors in the EV3 kit that we should learn to use.
# Plug the touch and IR sensors into the numbered ports on the EV3 brick.
#

###############################################################################
# 1. The touch sensor
#    This is a simple switch.
###############################################################################

touch_sensor = TouchSensor()
sound.speak('Please press the touch sensor')

## This is a 'while' loop. The condition after 'while' is tested each time the indented code runs 
while True:                             # <- The condition here is "True". This means the loop runs continuously.
    if touch_sensor.is_pressed == True: # <- This is a condition. The 'break' code underneath runs if the condition is true.
        break                           # <- This "jumps out" of the while loop.
    time.sleep(0.1)                     # <- What do you think this does?

#  The while loop above runs until you press the switch. And then we...
sound.play('breaking_glass.wav')

## Note that we could have written the while loop in fewer lines of code. Read 
## these lines and see if they make sense
#while not touch_sensor.is_pressed:
#    time.sleep(0.1)


###############################################################################
# 2. The infrared sensor
#    This sensor can tell you how far away an object is (it's not very accurate).
############################################################################### 

#
# 2.1 Uncomment this code to see how the IR sensor detects distance
#

#range_sensor = InfraredSensor()
#while True:
#    print('%d \%\r' % (range_sensor.proximity)) # Display the distance on the screen.
#    time.sleep(0.5)

## How does the number on the screen change as you move your hand in front of it?
## The number (proximity) displays the percentage of the maximum range. 
##   - 0% should be really close to the sensor
##   - 100% should be around 70cm.

#
# 2.2 Uncomment this code to break a window :).
#

#range_sensor = InfraredSensor()
#while True:
#    if range_sensor.proximity < 100:           # <- Play a sound if an object is in front of the sensor.
#        sound.play('breaking_glass.wav')
#    time.sleep(0.1)

###############################################################################
# 3. The ultrasonic sensor
#    This sensor can tell you how far away an object is. It works in the same
#    way that bats and submarines detect objects around them. It's pretty accurate.
############################################################################### 

#
# 3.1 Uncomment this code to see how the ultrasonic sensor detects distance
#

#range_sensor = UltrasonicSensor()
#while True:
#    print (range_sensor.distance_centimeters)
#    print('%3.1f cm\r' % (range_sensor.distance_centimeters)) # Display the distance on the screen.
#    time.sleep(0.5)

## How does the number on the screen change as you move your hand in front of it?
## The number (proximity) displays the distance in centremetres. 

#
# 3.2 Uncomment this code to break a window :).
#

range_sensor = UltrasonicSensor()
while True:
    if range_sensor.distance_centimeters < 150:           # <- Play a sound if an object is in front of the sensor.
        sound.play('breaking_glass.wav')
    time.sleep(0.1)


###############################################################################
# 4. The colour sensor
#    This sensor tells you the colour of an object in front of it.
############################################################################### 

#
# 4.1 Uncomment this code to see how colour sensor detects colour.
#     The colour is displayed on the screen. The sensor works best when the sensor
#     is very close to an object (can you guess why?).
#

## This is a "dictionary". Just like a real disctionary, we use it to look things up.
## If we look up '5', the dictionary returns 'COLOR_RED' 
#color_names = {
#    0 : 'COLOR_NOCOLOR', 
#    1 : 'COLOR_BLACK', 
#    2 : 'COLOR_BLUE',
#    3 : 'COLOR_GREEN',
#    4 : 'COLOR_YELLOW',
#    5 : 'COLOR_RED',
#    6 : 'COLOR_WHITE',
#}

#color_sensor = ColorSensor()
#while True:
#    color_num = color_sensor.color      # <- color is stored as a number. Eg 1 is black. 5 is red (see dictionary above) 
#    color_name = color_names[color_num] # This is how we look up a dictionary
#    print(color_name)
#    time.sleep(0.5)
