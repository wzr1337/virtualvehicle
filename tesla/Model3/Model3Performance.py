

from tesla.Model3.body import Sedan
from baseClasses.virtualvehicle import Vehicle

class Model3Performance(Vehicle):
    def __init__(self):
        # body of the constructor
        self.body = Sedan()

    def simulate(self, speed):
        return super().simulate(speed)