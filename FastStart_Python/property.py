class Car:
    __wheels = 4

    @property
    def wheels(self):
        return self.__wheels
    @wheels.setter
    def wheels(self, value):
        print("Setting wheels")
        if value < 0:
            raise ValueError("Wheels cannot be negative")
        self.__wheels = value

    @wheels.deleter
    def wheels(self):
        print("Deleting wheels")
        self.__wheels = 0

car = Car()
print(car.wheels)

car.wheels = 5
print(car.wheels)

del car.wheels
print(car.wheels)

