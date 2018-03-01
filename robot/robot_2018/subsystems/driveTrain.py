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
        print(motors['leftMotor'].getSensorCollection())
        self.motors = motors
        self.drive = DifferentialDrive(motors['leftMotor'],motors['rightMotor'])
        self.drive.setSafetyEnabled(False)

    def move (self,spd,rot):
        #print("Spd" ,spd, "rot", rot)
        self.drive.arcadeDrive(spd,rot,False)
        #print("Left Position: %f"%(self.motors['leftMotor'].getSelectedSensorPosition(0)))
        #print("Right Position: %f"%(self.motors['rightMotor'].getSelectedSensorPosition(0)))
        
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.DriveControlled())