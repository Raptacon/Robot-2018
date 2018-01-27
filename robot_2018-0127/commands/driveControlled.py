# -*- coding: utf-8 -*-
import wpilib
from wpilib import command

class DriveControlled(command.Command):
    def __init__(self):
        super().__init__('DriveControlled')
        self.requires(self.getRobot().drivetrain)
    
    def execute (self):
        controller = self.getRobot().driveController
        x= -1 * (controller.getX())
        y= controller.getY()
        rot= controller.getZ()
        #print("output: x %0.02f, y %0.02f, rot %0.02f" % (x,y,rot))
        self.getRobot().drivetrain.move(x,y,rot)
        '''Joystick Values on NetworkTables'''
        self.getRobot().smartDashboard.putNumber("Joystick-X", x)
        self.getRobot().smartDashboard.putNumber("Joystick-Y", y)
        self.getRobot().smartDashboard.putNumber("Joystick-Z", rot)