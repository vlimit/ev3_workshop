#!/usr/bin/env python3

#
# Abstract MoveTank so we can use a higher-level interface
#

import os
import time

from ev3dev2.motor import *
from ev3dev2.sensor.lego import *

#
# Remember all of those left, righ, forward, reverse functions you made earlier?
# They're now in a new class called MyRobot. Take a look in myrobot.py to see them.
# We can use that code by importing myrobot.py here:
#
from myrobot import *

range_sensor = InfraredSensor()

robot = MyRobot(cm_per_rev=15.9, straight_speed=30, turning_speed=10)

# Here's a simple wandering robot... Can you make it smarter?
while True:
    if range_sensor.proximity > 50:
        robot.forward(10, brake=False, block=False)
    else:
        # If the robot gets too close to an object then...
        robot.reverse(10)
        robot.left(45)
