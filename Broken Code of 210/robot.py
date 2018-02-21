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
from wpilib.command import Command
from networktables import NetworkTables
import motorHelper
from wpilib import Encoder
from commands import autonomousPositions
#from commands import autonomous
#from commands import followjoystick




class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        Command.getRobot = lambda x = 0: self
        self.motorHelper = motorHelper
        self.robotMap = robotMap.RobotMap()
        self.createNetworkTables()
        self.createControllers()
        self.drivetrain = subsystems.driveTrain.DriveTrain()
        self.loader = subsystems.loader.Loader()
        self.timer = wpilib.Timer()
        self.loaderButton = wpilib.buttons.JoystickButton(self.driveController, self.robotMap.controllerMap.driveController['loaderToggleButton'])
        self.loaderButton.whenPressed(commands.loaderCommand.LoaderToggle())
        self.driveEncoder = Encoder(0,1)
        self.lifter=subsystems.lifter.Lifter()
        #make robot avaiable to commands
        wpilib.CameraServer.launch('vision.py:main')
        self.autonomousPositions=commands.autonomousPositions.AutonomousPositions()
        
    def teleopInit(self):
        print("initializing teleop drive")
        
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()
        print("second test here")
        
        self.autonomousPostions.start()
        
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.smartDashboard.putNumber("timer",self.timer.get())
        t=self.timer.get()
        if t <5.0:
            self.drivetrain.move(0,-.5)
        elif t<8.0:
            self.drivetrain.move(.5,0)
        elif t<15:
            self.drivetrain.move(0,.5)
        else:
            self.drivetrain.move(0,0)
         #Drive for two seconds
        #if self.timer.get() < 2.0:
           # self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        #else:
            #self.drive.arcadeDrive(0, 0)  # Stop robot
    
    def autoInit(self):
        print("auto init")
        self.timer.reset()
        self.timer.start()
        print("second test here")
        self.autonomous.start
        
       # self.autonomousPostions.start()
        
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
        
    def createNetworkTables(self):
        NetworkTables.initialize(server = "roborio-3200-frc.local")
        self.smartDashboard = NetworkTables.getTable("SmartDashboard")
        self.smartDashboard.putNumber("raptacon",3200)
        
        
    
        
        
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
