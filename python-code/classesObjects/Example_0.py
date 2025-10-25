class Vehicle:
    def __init__(self,car):
        self.car=car;
    def move(self):
        print("Start the Engine to Move...");
class Car(Vehicle):
    def car_name(self):
        print(f"Name of the car:{self.car}");
    def addSpeed(self):
        print("Limited speed upto 300km");
class ElectricCar:
    car_type=Vehicle;
    def __init__(self):
        self.car=self.car_type("Mahindra SUV Batman Edition");
    def add_Battery(self):
        print("Battery 1000mph");

electric_car=ElectricCar();
electric_car.add_Battery();
vehicle=Vehicle();
vehicle.move();
car=Car();
car.car_name();
