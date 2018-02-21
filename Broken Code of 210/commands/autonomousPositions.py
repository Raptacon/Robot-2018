# -*- coding: utf-8 -*-

'''Starting to write the different commands for the autonomous period'''
import wpilib
import magicbot
from magicbot import timed_state 
from robotpy_ext.autonomous import StatefulAutonomous
from subsystems.loader import loader
class AutonomousPositions(StatefulAutonomous):
    
    MOD_NAME = 'Autonomous Positions'
    DEFAULT = True
   
    def initialize(self):
       pass

    class LeftPosition():
        '''this isn't supposed to be blank, i plan to add in the necessary changes'''
        @timed_state(duration=.5,next_state='rot_right',first=True)
        def drive_forward(self):
            self.drivetrain.move(0,1)
      
        @timed_state(duration=.5,next_state='toggle_lifter')
        def rot_right(self):
            self.drivetrain.move(1,0)
      
        @timed_state(duration=.5,next_state='toggle_loader')
        def toggle_lifter(self):
            self.lifter.move(1)
        
    
    