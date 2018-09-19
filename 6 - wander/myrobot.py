#!/usr/bin/env python3

#
# Abstract MoveTank so we can use a higher-level interface
#

import os
import time

from ev3dev2.motor import *

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

CM_PER_REV = 15.3
STRAIGHT_SPEED = 50
TURNING_SPEED = 20

class MyRobot:

    def __init__(self, cm_per_rev=15.9, straight_speed = STRAIGHT_SPEED, turning_speed = TURNING_SPEED):
        self.cmPerRev      = cm_per_rev
        self.straightSpeed = straight_speed
        self.turningSpeed  = turning_speed

    def forward(self, distance, speed=None, brake=True, block=True):
        '''distance: in cm'''

        if speed == None:
            speed = self.straightSpeed

        # If distance is -ve, then go backwards
        if distance < 0:
            speed = -speed

        tank_drive.on_for_rotations(
            SpeedPercent(speed),
            SpeedPercent(speed),
            abs(distance)/self.cmPerRev,
            brake=brake, 
            block=block
        )

    def reverse(self, distance, speed=None, brake=True, block=True):
        '''distance: in cm'''

        if speed == None:
            speed = self.straightSpeed

        # We're going backwards
        speed = -speed

        # If distance is -ve, then go forwards
        if distance < 0:
            speed = -speed

        tank_drive.on_for_rotations(
            SpeedPercent(speed),
            SpeedPercent(speed),
            abs(distance)/self.cmPerRev,
            brake=brake, 
            block=block
        )

    def left(self, angle=90, speed=None):
        '''angle: in degrees'''

        if speed == None:
            speed = self.turningSpeed

        tank_drive.on_for_rotations(
            SpeedPercent(speed),
            SpeedPercent(-speed),
            0.3 * angle / 90
        )

    def right(self, angle=90, speed=None):
        '''angle: in degrees'''

        if speed == None:
            speed = self.turningSpeed

        tank_drive.on_for_rotations(
            SpeedPercent(-speed),
            SpeedPercent(speed),
            0.3 * angle / 90
        )


