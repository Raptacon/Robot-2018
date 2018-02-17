# -*- coding: utf-8 -*-
import wpilib
import wpilib.buttons
import ctre
from ctre import WPI_TalonSRX

class RobotMap():
    def __init__(self):
        self.CAN = CANMap()
        self.controllerMap = ControllerMap()
        self.pneumatics = Pneumatics()
        
        
class CANMap():
    def __init__(self):
        pid = None
        motors = {}
        #pid = createPidVelDict(9000,0.0,0,0,WPI_TalonSRX.ControlMode.Velocity, ctre.FeedbackDevice.QuadEncoder, False)
        motors['leftMotor'] = {'channel':1, 'inverted': True, 'type':'CANTalon', 'pid':pid}
        
        motors['leftFollower']  = {'channel':2, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':1}
        #pid = createPidVelDict(9000,0.0,0,0,WPI_TalonSRX.ControlMode.Velocity, ctre.FeedbackDevice.QuadEncoder, False)
        motors['rightMotor'] = {'channel':0, 'inverted': False, 'type':'CANTalon', 'pid':pid}
        motors['rightFollower']  = {'channel':3, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':0,'talonPid':True}

        
        self.driveMotors = motors
        motors={}
        motors['lifterMotor'] = {'channel':4, 'inverted': False, 'type':'CANTalon'}
        motors['lifterFollower']  = {'channel':5, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':4, 'talonPid':False}

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

        driveController['lifterDownAxis']= 4
        driveController['lifterUpAxis']=2

        self.driveController = driveController
        
class Pneumatics():
    def __init__(self):
        self.pcmCAN = 1
        self.loader_open = 1
        self.loader_close = 0
      
        
def createPidVelDict(_100msVelCount, kP, kI, kD, controlType, feedbackType, sensorPhase = False, kInput = None):
    kF = 1023.0 / _100msVelCount
    if not kInput:
        kInput = _100msVelCount
    return {'kF':kF, 'kP':kP, 'kI':kI, 'kD':kD, 'kInput':kInput, 'controlType':controlType, 'feedbackType':feedbackType, 'sensorPhase':False}
        
#robotMap = RobotMap()
#robotMap = None        
