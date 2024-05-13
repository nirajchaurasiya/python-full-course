# Basic Class and Object
# Problem:
# Create a Car class with attributes like brand and model.
# Then create an instance of this class.


class Car:
    #  Class Variables
    # Problem: Add a class variable to Car that keeps
    # track of the number of cars created.
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    # Soln 2
    def fullname(self):
        return f"{self.__brand} {self.__model}"

    #  Polymorphism
    # Problem:
    # Demonstrate polymorphism by defining a method fuel_type
    # in both Car and ElectricCar classes, but with different behaviors.

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


# Inheritance
# Problem:
# Create an ElectricCar class that inherits from the Car
# class and has an additional attribute battery_size.
# Soln 3


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    #  Polymorphism
    # Problem:
    # Demonstrate polymorphism by defining a method fuel_type
    # in both Car and ElectricCar classes, but with different behaviors.

    def fuel_type(self):
        return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")

# print(isinstance(my_tesla, Car))

# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)

# print(my_tesla.fuel_type())

# print(my_tesla.model, my_tesla.brand, my_tesla.battery_size, my_tesla.fullname())


# my_car = Car("Toyota", "Corolla")

# # my_car.model = "City"

# print(my_car.model)

# print(Car.general_description())

# print(Car.total_car)


# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)

# print(my_car.model)

# print(my_car.fullname())

# my_new_car = Car("Tata", "Safari")

# print(my_new_car.brand)

# print(my_new_car.model)

# print(my_new_car.fullname())


class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")

print(my_new_tesla.engine_info())

print(my_new_tesla.battery_info())
