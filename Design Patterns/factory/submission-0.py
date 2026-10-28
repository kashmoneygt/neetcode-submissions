from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

# Concrete Vehicle implementations
class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

# Abstract VehicleFactory class
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

# Concrete Factory implementations
class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()

# Example usage
def main():
    car_factory = CarFactory()
    bike_factory = BikeFactory()
    truck_factory = TruckFactory()

    car = car_factory.createVehicle()
    bike = bike_factory.createVehicle()
    truck = truck_factory.createVehicle()

    print(car.getType())  # Output: Car
    print(bike.getType())  # Output: Bike
    print(truck.getType())  # Output: Truck

if __name__ == "__main__":
    main()
