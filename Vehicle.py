class Vehicle:
    counter=0
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        Vehicle.counter+=1
    def is_motor_vehicle():
        return "True"
    def get_vehicle_count():
        return Vehicle.counter
    def get_vehicle_age(self):
        return 2025-self.year
    def __repr__(self):
        return f"Vehicle('{self.make}','{self.model}',{self.year})"
