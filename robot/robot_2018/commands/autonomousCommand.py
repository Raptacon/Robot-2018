# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:52:03 2018

@author: cvalenzuelaacos
"""

from wpilib.command.commandgroup import CommandGroup

from wpilib.command.waitcommand import WaitCommand
from commands.moveRobot import MoveRobot
from commands.lifterCommand import LifterCommandTimed
from commands.loaderCommand import LoaderToggle


class AutonomousProgram(CommandGroup):
    '''
    A simple program that spins the motor for two seconds, pauses for a second,
    and then spins it in the opposite direction for two seconds.
    '''

    def __init__(self, robotLocation):
        super().__init__('Autonomous Program')
        self.robotLocation = robotLocation
        self.loaderState = self.getRobot().loader.State
        if self.getRobot().kCenter == robotLocation:
            print("Center Auto")
            self.createCenterCommands()
        elif self.getRobot().kLeft == robotLocation:
            print("Left auto")
            self.createLeftCommands()
        else:
            print("Right auto")
            self.createRightCommands()
        
    def createCenterCommands(self):
        self.addParallel(MoveRobot(-.5,.5, timeoutInSeconds=2.75))
        
    def createLeftCommands(self):
        self.createSideCommands()
        
        #if robot on side as field, maybe raise lifter and drop box?

    def createRightCommands(self):
        self.createSideCommands()
        #if robot on side as field, maybe raise lifter and drop box?        
        
    def createSideCommands(self):
        #move robot
              
        self.addSequential(LifterCommandTimed(.4, timeoutInSeconds=.5))
        self.addSequential(WaitCommand(1))
        self.addSequential(LoaderToggle(self.loaderState.kClose))

        self.addSequential(MoveRobot(-.5,.5, timeoutInSeconds=1))
        self.addSequential(MoveRobot(.5,-.5, timeoutInSeconds=1))
        self.addSequential(MoveRobot(-.5,.5, timeoutInSeconds=1.2))
        self.addParallel(LoaderToggle(self.loaderState.kOpen))

        self.addSequential(WaitCommand(0.5))

        self.addSequential(LoaderToggle(self.loaderState.kClose))
        self.addSequential(MoveRobot(.5,-.5, timeoutInSeconds=1.2))
        self.addSequential(WaitCommand(2))
        self.addSequential(LifterCommandTimed(0.4, timeoutInSeconds = 3))
        self.addParallel(MoveRobot(-.5,.5,timeoutInSeconds = 2.6))
        self.addSequential(WaitCommand(3))
        
        #drop box if needed
        self.createDropBoxCommands()
        #self.addSequential(LoaderToggle())
        self.addSequential(LifterCommandTimed(0.3, timeoutInSeconds = 1))
        self.addSequential(LifterCommandTimed(0.27, timeoutInSeconds = 2))
        #self.addSequential(WaitCommand(1))
        self.addParallel(MoveRobot(.5,-.5, timeoutInSeconds=1))
        
        #AND lift lifter
        
        #sync commands
        #elf.addSequential(MoveRobot(0,0, timeoutInSeconds = 0))
        #self.addSequential(LifterCommandTimed(0, timeoutInSeconds = 0))
        #let robot stablize
        #self.addSequential(WaitCommand(5.0))
        
        
        
        
    def createDropBoxCommands(self):
        #wait for robot to stablize
        
        #opend loader
        if(self.getRobot().ourSwitchSide == self.robotLocation):
            print("Adding box drop command")
            self.addSequential(LoaderToggle())
        else:
            print("Robot on wrong side. Not dropping box")
        self.addSequential(WaitCommand(1.0))
        
       # toggleDropBox=self.getRobot().smartDashboard.getNumber("toggleDropBox", 1)
    def initialize(self):
        print("Cmmand group stard")
        
        
