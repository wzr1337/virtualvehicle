from abc import ABC, abstractmethod, abstractproperty

from src.baseClasses.body import Body

class Vehicle(ABC):

    body: Body

    @abstractmethod
    def simulateStep(self, speed_meters_per_second, acceleration_meters_per_square_second=0, timestep_seconds = 1):
        return self.body.get_energy_flow(speed_meters_per_second, acceleration_meters_per_square_second)