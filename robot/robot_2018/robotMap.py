# -*- coding: utf-8 -*-
import wpilib



class RobotMap():
    def __init__(self):
        self.CAN = CANMap()
        self.controllerMap = ControllerMap()
        self.pneumatics = Pneumatics()
        
        
class CANMap():
    def __init__(self):
        motors = {}
        motors['frontRightMotor'] = {'channel':0, 'inverted':True, 'type':'CANTalon'}
        motors['frontLeftMotor']  = {'channel':1, 'inverted':False, 'type':'CANTalon'}
        motors['rearRightMotor']  = {'channel':2, 'inverted':True, 'type':'CANTalon'}
        motors['rearLeftMotor']   = {'channel':3, 'inverted':False, 'type':'CANTalon'}
        self.driveMotors = motors
        #add shooter motors to shooter.Motors
        
        
        
class ControllerMap():
    def __init__(self):
        self.controller1=wpilib.Joystick(0)
        self.controller2=wpilib.Joystick(1)
        
        self.controller1.setXChannel(0)
        self.controller1.setYChannel(1)
        self.controller1.setZChannel(4)
        self.controller1.setTwistChannel(5)
        
        self.controller1.setThrottleChannel(3)

class Pneumatics():
    def __init__(self):
        self.pcmCAN = 1
        self.loader_open = 1
        self.loader_close = 0
            
        
robotMap = RobotMap()
        
