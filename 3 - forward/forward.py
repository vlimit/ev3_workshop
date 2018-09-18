#!/usr/bin/env python3

#
# Introduction to tank drive. Work out the parameters to go forward, backward,
# left & right.
#

import os
import time

# Motors! This is getting interesting now :).
from ev3dev2.motor import *

# Guess what this does. How does a tank work? And what are your motors connected to?
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# Let's drive the robot (I mean tank):
tank_drive.on_for_rotations(
    SpeedPercent(20),   # left motor speed
    SpeedPercent(20),   # right motor speed
    1.0                 # number of wheel revolutions (of the fastest wheel)
)

# Exercises (write down all the parameters you used on the paper handout)

# 1. How far (cm) does it go in one wheel revolution?

# 2. How wide is a wheel?

# 3. How far apart are the wheels?

# 4. Can you make it go faster?

# 5. Can you make it go backwards?

# 6. Can you make it turn 90 degrees left?

# 7. Can you make it turn 90 degrees right?
