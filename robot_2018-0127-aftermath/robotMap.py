# -*- coding: utf-8 -*-
import wpilib
import wpilib.buttons


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
        #motors['rearRightMotor']  = {'channel':2, 'inverted':True, 'type':'CANTalon'}
        #motors['rearLeftMotor']   = {'channel':3, 'inverted':False, 'type':'CANTalon'}
        self.driveMotors = motors
        #add shooter motors to shooter.Motors
        
        
        
class ControllerMap():
    def __init__(self):
        driveController = {}
        driveController['controllerId'] = 0
        driveController['xAxis'] = 0
        driveController['yAxis'] = 1
        driveController['zAxis'] = 4
        driveController['twistAxis'] = 5
        driveController['throttleAxis'] = 3
        driveController['loaderToggleButton']= 1
        self.driveController = driveController
        
class Pneumatics():
    def __init__(self):
        self.pcmCAN = 1
        self.loader_open = 1
        self.loader_close = 0
            
        
#robotMap = RobotMap()
#robotMap = None        
