#!/usr/bin/env python3

#
# Abstract MoveTank so we can use a higher-level interface
#

import os
import time

from ev3dev2.motor import *

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# There's a lot to remember when using tank_drive. Let's make our lives easier
# by defining some functions that are useful for driving through a maze.
# Remember those numbers you wrote down on a piece of paper in the last
# exercise? You're going to need them to fix up the left/right/forward/backward
# functions below...

# lets start with defining the number of cm per revolution. What did you measure
# in exercise 1 in the last activity?

CM_PER_REV = 1.0

# Here are some variables that might be useful later on.
STRAIGHT_SPEED = 90
TURNING_SPEED = 20

def forward(distance):
    '''distance: in cm'''

    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        distance/CM_PER_REV # number of revolutions (of the fastest wheel)
    )

# In exercise 5 you worked out how to make the motors go backwards. Change the 
# parameters in the code below to make the robot goes backwards.
def backward(distance):
    '''distance: in cm'''
    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        distance/CM_PER_REV # number of revolutions (of the fastest wheel)
    )

# In execrise 6 you worked out the parameters to turn 90 degrees left. Change
# the parameters in the code below to turn left.
def left(angle=90):
    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        1.0                 # number of revolutions (of the fastest wheel)
    )

# In execrise 7 you worked out the parameters to turn 90 degrees left. Change
# the parameters in the code below to turn left.
def right(angle=90):
    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        1.0                 # number of revolutions (of the fastest wheel)
    )

# What shape would the robot trace out with these instructions?
forward(10)
left()
forward(10)
left()
forward(10)
left()
forward(10)

# Try again with a different speed. You could try using the STRAIGHT_SPEED
# and TURNING_SPEED variables to save you changing the same number in many
# places.
