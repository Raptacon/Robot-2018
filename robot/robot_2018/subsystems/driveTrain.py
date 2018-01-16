# -*- coding: utf-8 -*-
import wpilib
from wpilib.command.subsystem import Subsystem 
from wpilib.drive.mecanumdrive import MecanumDrive
#from wpilib.drive.mechanumDrive import MecanumDrive

import ctre 
from robotMap import RobotMap
import commands

class DriveTrain(Subsystem):
    def __init__(self):
        super().__init__('DriveTrain')
        map=RobotMap()
        motors={} 
        for name in map.CAN.driveMotors:
            motor=map.CAN.driveMotors[name]
            motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
            #motors[name].setInverted(motor['inverted'])
        
        self.drive = MecanumDrive(motors['frontLeftMotor'],motors['rearLeftMotor'],motors['frontRightMotor'],motors['rearRightMotor']) 

    def move (self,x,y,rot):
        self.drive.driveCartesian(x,y,rot,0)    
    
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.DriveControlled())