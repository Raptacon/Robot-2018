# -*- coding: utf-8 -*-

import wpilib

import ctre 



def createMotor(motorDescp):
    
    if motorDescp['type'] == 'CANTalon':
        motor = ctre.wpi_talonsrx.WPI_TalonSRX(motorDescp['channel'])
        motor.setInverted(motorDescp['inverted'])
        #if we want to use the built in encoder set it here
        if('talonPid' in motorDescp and motorDescp['talonPid']):
            motor.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder, 0, 10)
            
        return motor
    elif motorDescp['type'] == 'CANTalonFollower':
        motor =ctre.wpi_talonsrx.WPI_TalonSRX(motorDescp['channel'])
        motor.setInverted(motorDescp['inverted'])
        motor.set(ctre.wpi_talonsrx.ControlMode.Follower, motorDescp['masterChannel'])
        
    else:
        print("Unknown Motor")


#motor=map.CAN.driveMotors[name]
#            motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
#            motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
#            
#            motors[name] = wpilib.PWMSpeedController(motor['channel'])
#            