# -*- coding: utf-8 -*-
import wpilib
from wpilib.command.subsystem import Subsystem 
from wpilib.drive import DifferentialDrive
#from wpilib.drive.mechanumDrive import MecanumDrive
import commands


class DriveTrain(Subsystem):
    def __init__(self):
        super().__init__('DriveTrain')
        map=wpilib.command.Command.getRobot().robotMap
        
        #create motors here
        motors={} 
        for name in map.CAN.driveMotors:
            motors[name] = wpilib.command.Command.getRobot().motorHelper.createMotor(map.CAN.driveMotors[name])
        
        self.drive = DifferentialDrive(motors['leftMotor'],motors['rightMotor'])

    def move (self,rot,spd):
        self.drive.arcadeDrive(rot,spd)    
        
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.DriveControlled())