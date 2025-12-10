class Car(Vehicle):
    def __init__(self,make,model,year,doors):
        Vehicle.__init__(self,make,model,year)
        self.doors=doors
    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.doors} doors"
    def is_sedan(self):
        if self.doors==4:
            return True
        else:
            return False
