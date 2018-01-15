#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
from wpilib import RobotDrive
from robotMap import RobotMap
import ctre

import commandbased
import subsystems 
from wpilib.command import Command

#from commands import autonomous
#from commands import followjoystick

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        Command.getRobot = lambda x = 0: self
        self.drivetrain = subsystems.driveTrain.DriveTrain()
        self.loader = subsystems.loader.Loader()
        
    def teleopInit(self):
        print("TeleopInit")
        
    def testInit(self):
        print("testInit started")
        self.loader.testLoader()
        
        print("testInit Done")
   
                
        
import sys       
def exit(retval):
    pass
    #sys.exit(retval)

if __name__ == '__main__':
    wpilib._impl.main.exit = exit
    wpilib.run(MyRobot)

