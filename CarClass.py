# The Car Class
class Car():
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
            """Initialize car attributes."""
            self.make = make
            self.model = model
            self.year = year

            # Fuel capacity and level in gallons.
            self.fuel_capacity = 15
            self.fuel_level = 0

    def fill_tank(self):
            """Fill gas tank to capacity."""
            self.fuel_level = self.fuel_capacity
            print("Fuel tank is full.")

    def drive(self):
            """Simulate driving."""
            print("The car is moving.")

# Creating an object from a class
my_car = Car('audi', 'a4', 2016)

# Accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

# Calling methods
my_car.fill_tank()
my_car.drive()

# Creating multiple objects
my_car = Car('audi', 'a4', 2016)
my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('toyota', 'tacoma', 2010)