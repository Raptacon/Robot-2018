# -*- coding: utf-8 -*-
import wpilib
from wpilib.command.subsystem import Subsystem 
from wpilib.drive import DifferentialDrive

#from wpilib.drive.mechanumDrive import MecanumDrive
import commands

import time

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
        self.minSpeedChange = 0.001
        self.timeRate = 0.2
        
        self.desired = {}
        self.desired['left'] = 0
        self.desired['right'] = 0
        self.current = {}
        self.current['left'] = 0
        self.current['right'] = 0
        
        self.lastUpdateTime = time.time()
        self.deadband = 0.1

    def setDeadband(self,deadband):
        self.drive.deadband = deadband
        
        
    
    def move (self,spd,rot):
        #print("Spd" ,spd, "rot", rot)
        self.drive.arcadeDrive(spd,rot,True)
        #print("Left Position: %f"%(self.motors['leftMotor'].getSelectedSensorPosition(0)))
        #print("Right Position: %f"%(self.motors['rightMotor'].getSelectedSensorPosition(0)))
        
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.DriveControlled())
        
        
    def moveTank (self, left, right):
        
        self.drive.tankDrive(left,right,True)

          
        


class HealthMonitor(Subsystem):
    def __init__(self):
        super().__init__("HMS")
        self.warnVoltage = 8
        self.critVoltage = 7
        self.robot = wpilib.command.Command.getRobot()
    def setVoltageLimit(self,voltage):
        self.minVoltage = voltage
    def rumbleOnLimits(self, voltage = True):
        
        if voltage and (self.warnVoltage > 0 or self.critVoltage > 0):
            volts  = self.robot.pdp.getVoltage()
            if volts < self.critVoltage:
                print("Voltage CRITICAL limit at ", volts)
                self.setRumbles(1.0)
            elif volts < self.warnVoltage:
                print("Voltage warning at ", volts)
                self.setRumbles(0.5)
            else:
                self.setRumbles(0.0)
                
                
    
    def setRumbles(self,value):
        self.robot.driveController.setRumble(wpilib.Joystick.RumbleType.kLeftRumble, value)
        self.robot.driveController.setRumble(wpilib.Joystick.RumbleType.kRightRumble, value)
        self.robot.auxController.setRumble(wpilib.Joystick.RumbleType.kLeftRumble, value)
        self.robot.auxController.setRumble(wpilib.Joystick.RumbleType.kRightRumble, value)
        
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.CurrentMonitor())
        
    