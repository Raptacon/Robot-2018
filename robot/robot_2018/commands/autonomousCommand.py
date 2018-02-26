# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:52:03 2018

@author: cvalenzuelaacos
"""

from wpilib.command.commandgroup import CommandGroup

from wpilib.command.waitcommand import WaitCommand
from commands.moveRobot import MoveRobot

class AutonomousProgram(CommandGroup):
    '''
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    '''

    def __init__(self, fieldState, robotLocation):
        super().__init__('Autonomous Program')
        self.fieldState = fieldState
        self.robotLocation = robotLocation
        if self.getRobot().kCenter == fieldState:
            print("Center Auto")
            self.createCenterCommands(fieldState)
        elif self.getRobot().kLeft == fieldState:
            print("Left auto")
            self.createLeftCommands()
        else:
            print("Right auto")
            self.createRightCommands()
        
    def createCenterCommands(self):
        self.addSequential(MoveRobot(.25,.5, timeoutInSeconds=1))
        
        self.addSequential(MoveRobot(0.7,0.0, timeoutInSeconds=1))
        self.addSequential(WaitCommand(timeout=0))
        
    def creeateLeftCommands(self):
        self.addSequential(MoveRobot(.75,0, timeoutInSeconds=1))
        
        #if robot on side as field, maybe raise lifter and drop box?

    def createRightCommands(self):
        self.addSequential(MoveRobot(.75,0, timeoutInSeconds=1))
        
        #if robot on side as field, maybe raise lifter and drop box?        
        
    def createDropBoxCommands(self):
        #raise lifter
        #delay
        #drive forward
        #open claw
        pass
        
    def initialize(self):
        print("Cmmand group stard")
        
        
