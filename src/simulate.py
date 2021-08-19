from src.tesla.Model3.Model3Performance import Model3Performance

def main():
    vehicle = Model3Performance()
    print(vehicle.simulateStep(speed_meters_per_second=10))
    return 1

if __name__ == "__main__":
    main()