#!/usr/bin/env python3

#
# Abstract MoveTank so we can use a higher-level interface
#

import os
import time

from ev3dev2.motor import *
from ev3dev2.sensor.lego import *

#
# Remember all of those left, right, forward, reverse functions you made earlier?
# They're now in a new class called MyRobot. Take a look in myrobot.py to see them.
# We can use that code by importing myrobot.py here:
#
from myrobot import *

class RangeSensor:
    def __init__(self, sensor):
        self.sensor = sensor

        if sensor.__class__ == UltrasonicSensor:
            self.range = self._ultrasonicRange
        elif sensor.__class__ == InfraredSensor:
            self.range = self._infraredRange
        else: 
            raise TypeError('Unknwon sensor type.')

    def range(self):
        '''Returns the approximate range, in cm.'''
        assert('Virtual range method has not been overridden by the sensor-specific function')

    def _ultrasonicRange(self):
        return self.sensor.distance_centimeters

    def _infraredRange(self):
        return self.sensor.proximity/100.0 * 70



# Work out what type of sensor you have and uncomment out the appropriate line.
#range_sensor = RangeSensor(InfraredSensor())
range_sensor = RangeSensor(UltrasonicSensor())

robot = MyRobot(cm_per_rev=15.9, straight_speed=30, turning_speed=10)

# Here's a simple wandering robot... Can you make it smarter?
while True:
    if range_sensor.range() > 10:
        robot.forward(10, brake=False, block=False)
    else:
        # If the robot gets too close to an object then...
        robot.reverse(10)
        robot.left(45)
