# -*- coding: utf-8 -*-
import wpilib
from wpilib.command.subsystem import Subsystem 
from wpilib.drive import DifferentialDrive
#from wpilib.drive.mechanumDrive import MecanumDrive
import ctre 
import commands

class DriveTrain(Subsystem):
    def __init__(self):
        super().__init__('DriveTrain')
        map=wpilib.command.Command.getRobot().robotMap
        
        #create motors here
        motors={} 
        for name in map.CAN.driveMotors:
            motor=map.CAN.driveMotors[name]
            motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
            #motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
            #motors[name] = wpilib.PWMSpeedController(motor['channel'])
            motors[name].setInverted(motor['inverted'])
        
        self.drive = DifferentialDrive(motors['frontLeftMotor'],motors['frontRightMotor']) 

    def move (self,x,y,rot):
        self.drive.arcadeDrive(x,y)    
        
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.DriveControlled())