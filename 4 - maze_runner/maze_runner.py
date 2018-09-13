#!/usr/bin/env python3

import os
import time

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank

tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

# There's a lot to remember when using tank_drive. Let's make our lives easier
# by defining some functions that are useful for driving through a maze.
# Remember those numbers you wrote down on a piece of paper in the last
# exercise? You're going to need them to fix up the left/right/forward/backward
# functions below...

# lets start with defining the number of cm per revolution. What did you measure
CM_PER_REV = 1.0

def forward(distance):
    '''distance: in cm'''

    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        distance/CM_PER_REV # number of revolutions (of the fastest wheel)
    )

def backward(distance):
    '''distance: in cm'''
    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        distance/CM_PER_REV # number of revolutions (of the fastest wheel)
    )

def left(angle=90):
    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        1.0                 # number of revolutions (of the fastest wheel)
    )

def right(angle=90):
    tank_drive.on_for_rotations(
        SpeedPercent(20),   # left motor speed
        SpeedPercent(20),   # right motor speed
        1.0                 # number of revolutions (of the fastest wheel)
    )

# What whape would the robot trace out with these instructions?
forward(10)
left()
forward(10)
left()
forward(10)
left()
forward(10)
