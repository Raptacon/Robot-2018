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
        self.drive.arcadeDrive(spd,rot,True)
        #print("Left Position: %f"%(self.motors['leftMotor'].getSelectedSensorPosition(0)))
        #print("Right Position: %f"%(self.motors['rightMotor'].getSelectedSensorPosition(0)))
        
    def initDefaultCommand(self):
        self.setDefaultCommand(commands.driveControlled.DriveControlled())
        
        
        
        


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
        
    