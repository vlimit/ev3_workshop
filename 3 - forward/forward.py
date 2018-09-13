#!/usr/bin/env python3

import os
import time

# Motors! This is getting interesting now :).
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank

# Guess what this does. How does a tank work? And what are your motors connected to?
tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)

# Let's drive the robot (I mean tank):
tank_drive.on_for_rotations(
    SpeedPercent(20),   # left motor speed
    SpeedPercent(-20),  # right motor speed
    1.0                 # number of revolutions (of the fastest wheel)
)

# Exercises (write down all the parameters you used)

# 1. How far (cm) does it go in one wheel revolution?

# 2. Can you make it go faster?

# 3. Can you make it go backwards?

# 4. Can you make it turn 90 degrees left?

# 5. Can you make it turn 90 degrees right?

# 6. How wide is a wheel?

# 7. How far apart are the wheels?

