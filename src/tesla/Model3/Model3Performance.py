

from src.tesla.Model3.body import Sedan
from src.baseClasses.virtualvehicle import Vehicle

class Model3Performance(Vehicle):
    name = "Tesla Model 3 Performance"

    def __init__(self):
        # body of the constructor
        self.body = Sedan()

    def simulateStep(self, speed_meters_per_second, acceleration_meters_per_square_second=0, timestep_seconds=1):
        print(f'Simulating {self.name}: v={speed_meters_per_second} m/s; a={acceleration_meters_per_square_second} m/s^2; delta_t={timestep_seconds} s')
        return super().simulateStep(speed_meters_per_second, acceleration_meters_per_square_second=acceleration_meters_per_square_second, timestep_seconds=timestep_seconds)
