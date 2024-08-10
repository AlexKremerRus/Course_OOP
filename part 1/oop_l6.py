class Data:
    def __init__(self):
        print("init")
        self.value = ""
    def __get__(self, instance, owner):
        print("get")

        return self.value
    def __set__(self, instance, value):
        print("set")

        self.value = value

class User:
    name = Data()
    surname = Data()

test = User()



class Temperature:
    def __init__(self, celsium):
        self._celsium = celsium

    def __get__(self, instance, owner):
        print("get")
        return self._celsium
    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("set")
        self._celsium = value

class Celsius:
    temperature = Temperature(0)

    def __init__(self, temperature):
        self.temperature = temperature

a=Celsius(10)
print(a.temperature) #10
a.temperature = 20
print(a.temperature) #20
a.temperature = -300
print(a.temperature) #Raises ValueError