import wpilib
import subsystems
from robotMap import robotMap
from wpilib import DoubleSolenoid
from wpilib.command.subsystem import Subsystem

class Loader(Subsystem):
    def __init__(self):
        super().__init__('loader subsystem')
        pneumatics = robotMap.pneumatics
        self.loaderSolenoid = DoubleSolenoid(pneumatics.pcmCAN, pneumatics.loader_open, pneumatics.loader_close)
    def toggleLoader(self):
        loaderState = self.loaderSolenoid.get()
        
        #kReverse state claw is closed
        #kForwar state claw is open
        
        #if claw is closed then open
        if loaderState == DoubleSolenoid.Value.kReverse:
            loaderState = DoubleSolenoid.Value.kForward
            print ("Opening Loader")
        #else if claw is open or not set then close
        else:
            loaderState = DoubleSolenoid.Value.kReverse
            print ("Closing Loader")
        self.loaderSolenoid.set(loaderState)
        
        
    def testLoader(self):
        print("Starting testLoader")
        self.toggleLoader()
        assert(self.loaderSolenoid.get() == DoubleSolenoid.Value.kReverse)
        wpilib.Timer.delay(5)
        self.toggleLoader()
        assert(self.loaderSolenoid.get() == DoubleSolenoid.Value.kForward)
        wpilib.Timer.delay(5)
        print("Finish testLoader")