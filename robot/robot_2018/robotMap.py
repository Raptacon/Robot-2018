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
        rampRate=.2
        #pid = createPidVelDict(9000,0.0,0,0,WPI_TalonSRX.ControlMode.Velocity, ctre.FeedbackDevice.QuadEncoder, False)
        motors={}
        currentLimits = {'absMax':60, 'absMaxTimeMs':200, 'maxNominal':45 }
        
        motors['leftMotor'] = {'channel':1, 'inverted': False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        
        motors['leftFollower']  = {'channel':2, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':1,"rampRate":rampRate}
        #pid = createPidVelDict(9000,0.0,0,0,WPI_TalonSRX.ControlMode.Velocity, ctre.FeedbackDevice.QuadEncoder, False)
        motors['rightMotor'] = {'channel':0, 'inverted': False, 'type':'CANTalon', 'pid':pid,"rampRate":rampRate}
        motors['rightFollower']  = {'channel':3, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':0,'talonPid':True,"rampRate":rampRate}

        for motor in motors:
            motors[motor]['currentLimits'] = currentLimits
        
        self.driveMotors = motors
        rampRate = 0.5
        motors={}
        currentLimits = {'absMax':40, 'absMaxTimeMs':200, 'maxNominal':80 }
        motors['lifterMotor'] = {'channel':4, 'inverted': False, 'type':'CANTalon', 'currentLimits':currentLimits,"rampRate":rampRate}
        currentLimits = {'absMax':20, 'absMaxTimeMs':100, 'maxNominal':30 }
        motors['lifterFollower']  = {'channel':5, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':4, 'talonPid':False, 'currentLimits':currentLimits,"rampRate":rampRate}
        motors['lifterFollower2']  = {'channel':6, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':4, 'talonPid':False, 'currentLimits':currentLimits,"rampRate":rampRate}
        self.lifterMotors=motors
        #add shooter motors to shooter.Motors
        
        
        
class ControllerMap():
    def __init__(self):
        driveController = {}
        driveController['controllerId'] = 0
        driveController['xAxis'] = 1
        driveController['yAxis'] = 5 #3 on sim 5 on frc
        driveController['zAxis'] = 2

        driveController['voltRumble'] = 8
        
        auxController={}
        auxController['controllerId']=1
        auxController['loaderToggleButton']= 1
        driveController['voltRumble'] = 8
        #auxController['lifterDownAxis']= 4
        #auxController['lifterUpAxis']=2

        auxController['lifterDownAxis']= 2
        auxController['lifterUpAxis']=3
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
