# -*- coding: utf-8 -*-
import wpilib
from wpilib import command
from robotMap import robotMap

class DriveControlled(command.Command):
    def __init__(self):
        super().__init__('DriveControlled')
        self.controller1=robotMap.controllerMap.controller1
        self.controller2=robotMap.controllerMap.controller2
        # old way self.controller2=wpilib.Joystick(map.joystickmap.controller2)
        self.requires(self.getRobot().drivetrain)
    
    def execute (self):
        x= self.controller1.getX()
        y= self.controller1.getY()
        rot= self.controller1.getZ()
     
        self.getRobot().drivetrain.move(x,y,rot)
