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
        motors={}
        currentLimits = {'absMax':75, 'absMaxTimeMs':100, 'maxNominal':40 }
        
        motors['leftMotor'] = {'channel':1, 'inverted': True, 'type':'CANTalon', 'pid':pid}
        
        motors['leftFollower']  = {'channel':2, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':1}
        #pid = createPidVelDict(9000,0.0,0,0,WPI_TalonSRX.ControlMode.Velocity, ctre.FeedbackDevice.QuadEncoder, False)
        motors['rightMotor'] = {'channel':0, 'inverted': False, 'type':'CANTalon', 'pid':pid}
        motors['rightFollower']  = {'channel':3, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':0,'talonPid':True}

        for motor in motors:
            motors[motor]['currentLimits'] = currentLimits
        
        self.driveMotors = motors
        motors={}
        currentLimits = {'absMax':100, 'absMaxTimeMs':100, 'maxNominal':40 }
        motors['lifterMotor'] = {'channel':4, 'inverted': False, 'type':'CANTalon', 'currentLimits':currentLimits}
        currentLimits = {'absMax':50, 'absMaxTimeMs':100, 'maxNominal':20 }
        motors['lifterFollower']  = {'channel':5, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':4, 'talonPid':False, 'currentLimits':currentLimits}
        motors['lifterFollower2']  = {'channel':6, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':4, 'talonPid':False, 'currentLimits':currentLimits}
        self.lifterMotors=motors
        #add shooter motors to shooter.Motors
        
        
        
class ControllerMap():
    def __init__(self):
        driveController = {}
        driveController['controllerId'] = 0
        driveController['xAxis'] = 0
        driveController['yAxis'] = 1
        driveController['voltRumble'] = 8
        
        auxController={}
        auxController['controllerId']=1
        auxController['loaderToggleButton']= 1
        driveController['voltRumble'] = 8
        #auxController['lifterDownAxis']= 4
        #auxController['lifterUpAxis']=2

        auxController['lifterDownAxis']= 3
        auxController['lifterUpAxis']=2
        self.driveController = driveController
        self.auxController = auxController
        
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
