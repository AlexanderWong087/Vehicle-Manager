
if __name__=="__main__":
    main()
def main():
    car1 = Car('Toyota', 'Camry', 2018, 4) 
    car2 = Car('Honda', 'Civic', 2020, 2) 
    truck1 = Truck('Ford', 'F-150', 2019, 2) 
    print(car1)
    print(repr(car1))
    print(truck1)
    print(repr(truck1)) 
    print(f"Car1 age: {car1.get_vehicle_age()} years") 
    print(f"Truck1 age: {truck1.get_vehicle_age()} years") 
    print(Car.is_motor_vehicle()) 
    print(f"Total vehicles: {Vehicle.get_vehicle_count()}") 
    print(f"Is Car1 a sedan? {car1.is_sedan()}") 
    print(f"Can Truck1 carry 3 tons? {truck1.can_carry_weight(3)}") 
