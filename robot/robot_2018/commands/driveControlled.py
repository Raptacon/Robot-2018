# -*- coding: utf-8 -*-
import wpilib
from wpilib import command
from wpilib import Encoder

class DriveControlled(command.Command):
    def __init__(self):
        super().__init__('DriveControlled')
        
        self.requires(self.getRobot().drivetrain)
        self.getRobot().smartDashboard.putNumber("Joystick-Right-Xscale", 1.0)
        self.getRobot().smartDashboard.putNumber("Joystick-Left-Yscale", 1.0)
        
        self.getRobot().smartDashboard.putNumber("deadZone", 0.1)
    def execute (self):
        controller = self.getRobot().driveController
        driveMap = self.getRobot().robotMap.controllerMap.driveController
        rightscale=self.getRobot().smartDashboard.getNumber("Joystick-Right-Xscale", 1.0)
        leftscale=self.getRobot().smartDashboard.getNumber("Joystick-Left-Yscale", 1.0)
       # rotscale=self.getRobot().smartDashboard.getNumber("Joystick-Zscale", 1)
        deadZone=self.getRobot().smartDashboard.getNumber("deadZone", 0.1) 
        #print("output: x %0.02f, y %0.02f, rot %0.02f" % (x,y,rot))
        self.getRobot().drivetrain.setDeadband(deadZone)
        '''Joystick Values on NetworkTables'''
        
        rightspeed=controller.getRawAxis(driveMap['rightTread'])
        
        #if (abs(controller.getY())<=deadZone):
        #    rotspeed=0
        leftspeed=controller.getRawAxis(driveMap['leftTread'])
        #if (abs(controller.getX())<=deadZone):
        #    spdspeed=0
        #rotspeed=controller.getZ()
       # if (abs(controller.getX())<deadZone):
         #   rotspeed=0
        
        left=rightscale*rightspeed
        right=leftscale*leftspeed
       # rot=rotscale*rotspeed
        self.getRobot().drivetrain.moveTank(left,right)
        self.getRobot().smartDashboard.putNumber("Joystick-left", left)
        self.getRobot().smartDashboard.putNumber("Joystick-right", right)
 
        #create motors here
        
        #self.getRobot().smartDashboard.putNumber("EncoderVal", encv)
        
        
        
       # self.getRobot().smartDashboard.putNumber("Joystick-Z", rot)
       
     
       
        
       
class CurrentMonitor(command.Command):
    def __init__(self):
        super().__init__("CurrentMonitorCmd")
        
        self.requires(self.getRobot().healthMonitor)
    def execute(self):
        self.getRobot().healthMonitor.rumbleOnLimits()
       
        