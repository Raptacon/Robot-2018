import wpilib
from wpilib import command
from wpilib import Encoder
from wpilib import XboxController

class LifterCommand(command.Command):
    def __init__(self):
        super().__init__('LifterCommand')
        
        self.requires(self.getRobot().lifter)
        self.getRobot().smartDashboard.putNumber("lifterSpeed", -1)
        self.getRobot().smartDashboard.putNumber("deadZone", 0.1) 
        self.controllerMap=self.getRobot().robotMap.controllerMap
        
    def execute (self):
        spd = self.getSpeed()
        self.getRobot().lifter.move(spd)
        self.getRobot().smartDashboard.putNumber("lifterSpeed", spd)
        
        
    def getSpeed(self):
        controller = self.getRobot().driveController
        upSpeed=controller.getRawAxis(self.controllerMap.driveController['lifterUpAxis'])
        downSpeed=controller.getRawAxis(self.controllerMap.driveController['lifterDownAxis'])
        spdscale=self.getRobot().smartDashboard.getNumber("lifterSpeed", -1)
        deadZone=self.getRobot().smartDashboard.getNumber("deadZone", 0.1) 
        
        self.getRobot().smartDashboard.putNumber("upSpeed", upSpeed)
        self.getRobot().smartDashboard.putNumber("downSpeed", downSpeed) 
        
        if (upSpeed>=deadZone and downSpeed>=deadZone):
            return 0 
        if (upSpeed>=deadZone):
            return upSpeed*spdscale
        if (downSpeed>=deadZone):
            return -downSpeed*spdscale
        return 0 
