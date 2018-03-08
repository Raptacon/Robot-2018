# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:46:17 2018

@author: cvalenzuelaacos
"""

from wpilib.command import TimedCommand
from wpilib.command import Command

import subsystems

class MoveRobot(Command):
    '''
    Spins the motor at the given power for a given number of seconds, then
    stops.
    '''

    def __init__(self, magnitude, rotation, timeoutInSeconds):
        super().__init__('Set Speed %d and rotation %d' % (magnitude,rotation), timeoutInSeconds)

        self.magnitude = magnitude
        self.rotation = rotation
        self.requires(Command.getRobot().drivetrain)
        print("Created timed command")
    def execute(self):

        #it seems like rot / magnitude is reversed, is this a bug in the robot lib sim?
        Command.getRobot().drivetrain.move(self.rotation, -self.magnitude)

    def end(self):
        #print("done")
        Command.getRobot().drivetrain.move(0,0)
        
    def isFinished(self):
        """Ends command when timed out."""
        return self.isTimedOut()
