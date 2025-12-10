class Truck(Vehicle):
    def __init__(self,make,model,year,capacity):
        Vehicle.__init__(self,make,model,year)
        self.capacity=capacity
    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.capacity} tons capacity"
    def can_carry_weight(self,weight):
        if self.capacity>=weight:
            return "True"
        else:
            return "False"
