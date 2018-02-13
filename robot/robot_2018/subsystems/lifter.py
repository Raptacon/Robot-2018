# -*- coding: utf-8 -*-
import wpilib
from wpilib.command.subsystem import Subsystem 
from wpilib.drive import DifferentialDrive
import commands


class Lifter(Subsystem):
    def __init__(self):
        super().__init__('Lifter')
        map=wpilib.command.Command.getRobot().robotMap
        
        #create motors here
        motors={} 
        for name in map.CAN.lifterMotors:
            motors[name] = wpilib.command.Command.getRobot().motorHelper.createMotor(map.CAN.lifterMotors[name])
       # print(motors['leftMotor'].getSensorCollection())
        self.motors = motors
        


    def move (self,spd):
        self.motors['lifterMotor'].set(spd)
        #print("Left Position: %f"%(self.motors['leftMotor'].getSelectedSensorPosition(0)))
        #print("Right Position: %f"%(self.motors['rightMotor'].getSelectedSensorPosition(0)))
        
    def initDefaultCommand(self):
        pass
        #self.setDefaultCommand(commands.driveControlled.DriveControlled())

