import wpilib
from wpilib import command
from wpilib.buttons import Trigger 
class LoaderToggle(wpilib.command.InstantCommand):
    def __init__(self, loaderState = None):
        super().__init__('LoaderToggle')
        self.loaderState = loaderState
        self.requires(self.getRobot().loader)
    def initialize(self):
        if(self.loaderState == None):
            self.getRobot().loader.toggleLoader()
        else:
            try:
                self.getRobot().loader.setLoader(self.loaderState)
            except Exception as err:
                print("Bad loader state", self.loaderState)
                print(err)
        
                    