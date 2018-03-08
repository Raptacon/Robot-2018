# -*- coding: utf-8 -*-
import wpilib
from wpilib import command
from wpilib import Encoder

class DriveControlled(command.Command):
    def __init__(self):
        super().__init__('DriveControlled')
        
        self.requires(self.getRobot().drivetrain)
        self.getRobot().smartDashboard.putNumber("Joystick-Yscale", -1)
        self.getRobot().smartDashboard.putNumber("Joystick-rotscale", 1)
        self.getRobot().smartDashboard.putNumber("deadZone", 0.1)
    def execute (self):
        controller = self.getRobot().driveController
        rotscale=self.getRobot().smartDashboard.getNumber("Joystick-Xscale", 1)
        spdscale=self.getRobot().smartDashboard.getNumber("Joystick-Yscale", -1)
       # rotscale=self.getRobot().smartDashboard.getNumber("Joystick-Zscale", 1)
        deadZone=self.getRobot().smartDashboard.getNumber("deadZone", 0.1) 
        #print("output: x %0.02f, y %0.02f, rot %0.02f" % (x,y,rot))
        
        '''Joystick Values on NetworkTables'''
        
        rotspeed=controller.getY()
        if (abs(controller.getY())<=deadZone):
            rotspeed=0
        spdspeed=controller.getX()
        if (abs(controller.getX())<=deadZone):
            spdspeed=0
        #rotspeed=controller.getZ()
       # if (abs(controller.getX())<deadZone):
         #   rotspeed=0
        
        rot=rotscale*rotspeed
        spd=spdscale*spdspeed
       # rot=rotscale*rotspeed
        self.getRobot().drivetrain.move(spd,rot)
        self.getRobot().smartDashboard.putNumber("Joystick-rot", rot)
        self.getRobot().smartDashboard.putNumber("Joystick-Y", spd)
 
        #create motors here
        
        #self.getRobot().smartDashboard.putNumber("EncoderVal", encv)
        
        
        
       # self.getRobot().smartDashboard.putNumber("Joystick-Z", rot)
       
     
       
        
       
class CurrentMonitor(command.Command):
    def __init__(self):
        super().__init__("CurrentMonitorCmd")
        
        self.requires(self.getRobot().healthMonitor)
    def execute(self):
        self.getRobot().healthMonitor.rumbleOnLimits()
       
        