import wpilib
import subsystems
import robotMap
from wpilib import DoubleSolenoid
from wpilib.command.subsystem import Subsystem
import enum
class Loader(Subsystem):
    def __init__(self, initialState = 0):
       #Loader.State.kClose
        super().__init__('loader subsystem')
        pneumatics = wpilib.command.Command.getRobot().robotMap.pneumatics
        self.loaderSolenoid = DoubleSolenoid(pneumatics.pcmCAN, pneumatics.loader_open, pneumatics.loader_close)
        #intialization: close the loader so we know where it begins at. 
        self.currentState=initialState
        self.setLoader(initialState)
    def toggleLoader(self):
        #if claw is closed then open
        if self.currentState==self.State.kOpen:
            loaderState = self.State.kClose
            print ("Opening Loader")
        #else if claw is open or not set then close
        else:
            loaderState = self.State.kOpen
        self.setLoader(loaderState)
        #self.getRobot().smartDashboard.putNumber("Loader Closed", loaderState)
        
    def testLoader(self):
        self.setLoader(self.State.kOpen)
        print("Starting testLoader")
        self.toggleLoader()
        assert(self.loaderSolenoid.get() == DoubleSolenoid.Value.kReverse)
        wpilib.Timer.delay(5)
        self.toggleLoader()
        assert(self.loaderSolenoid.get() == DoubleSolenoid.Value.kForward)
        wpilib.Timer.delay(5)
        print("Finish testLoader")
        self.toggleLoader()
        assert(self.loaderSolenoid.get() == DoubleSolenoid.Value.kReverse)
        wpilib.Timer.delay(2)
        print ("Finished testLoader now")
        
    def setLoader(self,state):
        #kReverse state claw is closed
        #kForward state claw is open
        if state == self.State.kOpen:
            self.loaderSolenoid.set(DoubleSolenoid.Value.kForward) 
        elif state ==self.State.kClose:
            self.loaderSolenoid.set(DoubleSolenoid.Value.kReverse) 
        else: 
            raise ValueError("Invalid Loader State %s" %value)
        self.currentState=state
        
        
    class State(enum.IntEnum):
        #state of the loader accuator
        kOpen=0
        kClose=1
        
    