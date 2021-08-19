from abc import ABC, abstractmethod, abstractproperty
from scipy import constants
import atmos

class Body(ABC):

    def __init__(self, c_W = 0.0, body_mass = 0.0, drag_area = 0.0, f_R=0.0):
        if 0.0 == c_W or 0.0 == body_mass or 0.0 == drag_area or 0.0 == f_R:
            print(f'model needs `c_W`, `body_mass`, drag_area` and `f_R` parameters')
            raise ValueError
        self.c_W = c_W
        self.body_mass = body_mass
        self.drag_area = drag_area
        self.f_R = f_R

    def __get_tractive_effort(self, v, a):
        self.speed = v
        self.acceleration = a
        F_friction = self.f_R * self.body_mass * constants.g
        F_acceleration = self.body_mass * a
        F_wind = self.c_W * atmos.calculate('rho', Tv=273., p=1e5) * self.drag_area * v*v
        F_longitudinal = F_friction + F_acceleration + F_wind
        return F_longitudinal

    @abstractmethod
    def get_energy_flow(self, speed_meters_per_second, acceleration_meters_per_square_second = 0.0):
        F = self.__get_tractive_effort(speed_meters_per_second, acceleration_meters_per_square_second)
        return {
            "potential": {
                "value": F,
                "unit": "N"
            },
            "flow": {
                "value": speed_meters_per_second,
                "unit": "m/s"
            },
            "power": {
                "value": F * self.speed,
                "unit": "Watt"
            }
        }
