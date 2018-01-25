#!/usr/bin/env python3
'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import wpilib
from wpilib import RobotDrive
import robotMap
import ctre
import commands
import commandbased
import subsystems 
import wpilib.buttons
from wpilib.command import Command

#from commands import autonomous
#from commands import followjoystick

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        self.robotMap = robotMap.RobotMap()
        self.createControllers()
        
        #make robot avaiable to commands
        Command.getRobot = lambda x = 0: self
         
        self.drivetrain = subsystems.driveTrain.DriveTrain()
        self.loader = subsystems.loader.Loader()
        self.timer = wpilib.Timer()
        
        
        self.loaderButton = wpilib.buttons.JoystickButton(self.driveController, 
                                                          self.robotMap.controllerMap.driveController['loaderToggleButton'])
        self.loaderButton.whenPressed(commands.loaderCommand.LoaderToggle())
        
    def teleopInit(self):
        print("initializing teleop drive")
        
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()
        print("second test here")
        
        
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        wpilib.Timer.delay(5)
        print("periodic tick")
        # Drive for two seconds
        #if self.timer.get() < 2.0:
           # self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        #else:
            #self.drive.arcadeDrive(0, 0)  # Stop robot
    def autoInit(self):
        print("auto init")
        
        
    def testInit(self):
        print("testInit started")
        self.loader.toggleLoader()
        self.loader.testLoader()
        print("testInit Done")
        
                
        
    def createControllers(self):
        '''
        create the joysticks instances and assign axis from controller channels.
        '''
        controllerMap = self.robotMap.controllerMap
        driveController = controllerMap.driveController
        
        self.driveController=wpilib.Joystick(driveController['controllerId'])
        
        self.driveController.setXChannel(driveController['xAxis'])
        self.driveController.setYChannel(driveController['yAxis'])
        self.driveController.setZChannel(driveController['zAxis'])
        self.driveController.setTwistChannel(driveController['twistAxis'])
        
        self.driveController.setThrottleChannel(driveController['throttleAxis'])
        
        
        
#import sys       
def exit(retval):
    pass
#    sys.exit(retval)

if __name__ == '__main__':
    try:
        print(wpilib._impl.main.exit)
    except:
        wpilib._impl.main.exit = exit
    wpilib.run(MyRobot,physics_enabled=True)

