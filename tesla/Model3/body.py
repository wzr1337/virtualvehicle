from baseClasses.body import Body

class Sedan(Body):
    def __init__(self, Name="Tesla Model 3 Performance", c_W = 0.23, body_mass = 1800, drag_area = 2.22, f_R = 0.015):
        super().__init__(Name=Name, c_W=c_W, body_mass=body_mass, drag_area=drag_area, f_R=f_R)
        print(f'Initialzing `{Name}`')

    def get_energy_flow(self, speed_meters_per_second, acceleration_meters_per_square_second):
        return super().get_energy_flow(speed_meters_per_second, acceleration_meters_per_square_second=acceleration_meters_per_square_second)