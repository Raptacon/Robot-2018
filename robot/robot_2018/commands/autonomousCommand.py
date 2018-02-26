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

    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(MoveRobot(0.5,0, timeoutInSeconds=2))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(MoveRobot(0.2,.3, timeoutInSeconds=1))
        self.addSequential(WaitCommand(timeout=0))
        print("Robot auto created")
        #self.addSequential(WaitCommand(timeout=1))
        #self.addSequential(MoveRobot(.5,1.0, timeoutInSeconds=1))
        
    def initialize(self):
        print("Cmmand group stard")
        
        
