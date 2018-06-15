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
from wpilib import DriverStation
from wpilib.command import Command
import wpilib.command
from networktables import NetworkTables
import motorHelper
from wpilib import Encoder

#from commands import autonomous
#from commands import followjoystick

 


class MyRobot(commandbased.CommandBasedRobot):
    
    kLeft = 0
    kCenter = 1
    kRight = 2
    kNothing=4
    def robotInit(self):
        Command.getRobot = lambda x = 0: self
        self.driverStation = DriverStation.getInstance()
        self.motorHelper = motorHelper
        self.robotMap = robotMap.RobotMap()
        self.createNetworkTables()
        self.createControllers()
        self.drivetrain = subsystems.driveTrain.DriveTrain()
        self.loader = subsystems.loader.Loader()
        self.timer = wpilib.Timer()
        self.loaderButton = wpilib.buttons.JoystickButton(self.auxController, self.robotMap.controllerMap.auxController['loaderToggleButton'])
        self.loaderButton.whenPressed(commands.loaderCommand.LoaderToggle())

        self.pdp = wpilib.PowerDistributionPanel()
        self.healthMonitor = subsystems.driveTrain.HealthMonitor()
        self.lifter=subsystems.lifter.Lifter()
        #make robot avaiable to commands
        wpilib.CameraServer.launch('vision.py:main')
        self.smartDashboard.putString('field position' ,"Enter L, R, or C,N")
        
        self.loader.setLoader(self.loader.State.kOpen)
       # self.Encoder = Encoder(0,1)
        
        
    def teleopInit(self):
        print("initializing teleop drive")
        
    def autonomousInit(self):       
        """This function is run once each time the robot enters autonomous mode."""
        fieldState = self.driverStation.getGameSpecificMessage()
        self.fieldState = fieldState
        self.smartDashboard.putString("field state", fieldState)
        fieldPosition = self.smartDashboard.getString("field position", "")
        self.startingFieldPosition = self.parserobotFieldPosition(fieldPosition)
        self.smartDashboard.putNumber("position", self.startingFieldPosition)
    
        #convert field states to our enum values    
        self.ourSwitchSide = self.parserobotFieldPosition(self.fieldState[0])
        self.scaleSide = self.parserobotFieldPosition(self.fieldState[1])
        self.theirSwitchSide = self.parserobotFieldPosition(self.fieldState[2])
        if self.startingFieldPosition==self.kNothing:
            print("No field position set. Aborting")
            return 
        
        
        #self.Encoder.setMaxPeriod(.1)
        #self.Encoder.setMinRate(10)
        #self.Encoder.setDistancePerPulse(5)
        #self.Encoder.setReverseDirection(True)
        #self.Encoder.getDistance()
        
        """self.Encoder.reset()
        while (self.Encoder.get() < value):
          drive
          delay"""
        
        
        
        
        
        
        
        #self.Encoder.getRawAxis()
        
        
        #todo change RRR to from fms, maybe parse it first
        
        self.autonomousProgram = commands.autonomousCommand.AutonomousProgram(self.startingFieldPosition)
        self.autonomousProgram.start()
    
    def testInit(self):
        '''print("testInit started")
        self.loader.toggleLoader()
        self.loader.testLoader()
        print("testInit Done")'''
        pass
                
        
    def createControllers(self):
        '''
        create the joysticks instances and assign axis from controller channels.
        '''
        controllerMap = self.robotMap.controllerMap
        driveController = controllerMap.driveController
        auxControllerMap = controllerMap.auxController
        self.driveController=wpilib.Joystick(driveController['controllerId'])
        self.auxController=wpilib.Joystick(auxControllerMap['controllerId'])
        #self.driveController.setXChannel(driveController['rightTread'])
        #self.driveController.setYChannel(driveController['leftTread'])
        
        
    def createNetworkTables(self):
        NetworkTables.initialize(server = "roborio-3200-frc.local")
        self.smartDashboard = NetworkTables.getTable("SmartDashboard")
        self.smartDashboard.putNumber("raptacon",3200)
        
    def parserobotFieldPosition(self, fieldPosition):
        fieldPosition = fieldPosition.lower().strip()
        if fieldPosition[0] == "l":
            return self.kLeft
        if fieldPosition[0] == "r":
            return self.kRight
        if fieldPosition[0] == "c":
            return self.kCenter
        
        print ("unable to read field position:",fieldPosition, "Using default kNothing")
        return self.kNothing
        
        
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
