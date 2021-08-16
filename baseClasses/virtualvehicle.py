from abc import ABC, abstractmethod, abstractproperty
from baseClasses.body import Body

class Vehicle(ABC):

    body: Body

    @abstractmethod
    def simulate(self, speed):
        return self.body.get_energy_flow(speed, -1)