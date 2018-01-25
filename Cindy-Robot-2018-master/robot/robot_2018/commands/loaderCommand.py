import wpilib

class LoaderToggle(wpilib.command.InstantCommand):
    def __init__(self):
        super().__init__('LoaderToggle')
        self.requires(self.getRobot().loader)
    def initialize(self):
        self.getRobot().loader.toggleLoader()



