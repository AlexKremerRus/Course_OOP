class Car:
    __BRAND = 'BMW'

    def __init__(self, color, price):
        self.__color = color
        self.__price = price

    @property
    def brand(self):
        return self.__BRAND

    @classmethod
    def set_brand(cls, brand):
        cls.__BRAND = brand


car = Car('red', 1000)
car2 = Car('blue', 2000)
print(car.brand)
car.set_brand('lada')
print(car.brand)
print(car2.brand)