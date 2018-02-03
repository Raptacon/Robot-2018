# -*- coding: utf-8 -*-

import wpilib

import ctre 



def createMotor(motorDescp):
    
    if motorDescp['type'] == 'CANTalon':
        motor = ctre.wpi_talonsrx.WPI_TalonSRX(motorDescp['channel'])
        motor.setInverted(motorDescp['inverted'])
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