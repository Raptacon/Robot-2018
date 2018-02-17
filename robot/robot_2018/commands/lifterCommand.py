# -*- coding: utf-8 -*-


import wpilib
from wpilib import command
from wpilib import Encoder
from wpilib import XboxController

class LifterCommand(command.Command):
    def __init__(self):
        super().__init__('LifterCommand')
        
        self.requires(self.getRobot().lifter)
        self.getRobot().smartDashboard.putNumber("lifter-Speed", 1)
        self.getRobot().smartDashboard.putNumber("lifter-deadZone", 0.1) 
        self.controllerMap=self.getRobot().robotMap.controllerMap
        self.highLimitSwitch = wpilib.DigitalInput(8)
        self.lowLimitSwitch = wpilib.DigitalInput(9)
        
    def execute (self):
        spd = self.getSpeed()
        self.getRobot().lifter.move(spd)
        self.getRobot().smartDashboard.putNumber("lifterSpeed", spd)
        print("I AM HERE")
        
    def getSpeed(self):
        controller = self.getRobot().driveController
        upSpeed=controller.getRawAxis(self.controllerMap.driveController['lifterUpAxis'])
        downSpeed=controller.getRawAxis(self.controllerMap.driveController['lifterDownAxis'])
        spdscale=self.getRobot().smartDashboard.getNumber("lifter-Speed", 1)
        deadZone=self.getRobot().smartDashboard.getNumber("lifter-deadZone", 0.1) 
        
        self.getRobot().smartDashboard.putNumber("upSpeed", upSpeed)
        self.getRobot().smartDashboard.putNumber("downSpeed", downSpeed)
        self.getRobot().smartDashboard.putString("high limit switch", self.highLimitSwitch.get())
        self.getRobot().smartDashboard.putString("low limit switch", self.lowLimitSwitch.get())
        
        
        lifterSpeed = 0
        if(upSpeed <= deadZone) or (self.highLimitSwitch.get()):
            upSpeed = 0
        if(downSpeed <= deadZone) or (self.lowLimitSwitch.get()):
            downSpeed = 0
        lifterSpeed = ((upSpeed - downSpeed) * spdscale)
        '''if (upSpeed>=deadZone and downSpeed>=deadZone):
            lifterSpeed = 0
        elif (upSpeed>=deadZone):
            lifterSpeed = upSpeed*spdscale
        elif (downSpeed>=deadZone):
            lifterSpeed = -downSpeed*spdscale'''
    
        self.getRobot().smartDashboard.putNumber("lifter-MotorSpeed", lifterSpeed)
        
        return lifterSpeed
        