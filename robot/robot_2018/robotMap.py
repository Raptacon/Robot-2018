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
        motors['leftMotor'] = {'channel':1, 'inverted': True, 'type':'CANTalon'}
        motors['leftFollower']  = {'channel':2, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':1, 'talonPid':True}
        motors['rightMotor'] = {'channel':0, 'inverted': False, 'type':'CANTalon'}
        motors['rightFollower']  = {'channel':3, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':0,'talonPid':True}

        
        self.driveMotors = motors
        motors={}
        motors['lifterMotor'] = {'channel':10, 'inverted': False, 'type':'CANTalon'}
        motors['lifterFollower']  = {'channel':12, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':10, 'talonPid':False}
        self.lifterMotors=motors
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
        driveController['lifterDownAxis']= 3
        driveController['lifterUpAxis']=2        
        
        self.driveController = driveController
        
class Pneumatics():
    def __init__(self):
        self.pcmCAN = 1
        self.loader_open = 1
        self.loader_close = 0
            
        
#robotMap = RobotMap()
#robotMap = None        
