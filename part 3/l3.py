class User:
    def __init__(self, value):
        self.value = value
        self.arrage = [1,2,3,4]
    def __pow__(self, power, modulo=None):
        return self.value**power
    def __reversed__(self):
        self.arrage.reverse()
        return self.arrage
    def __truediv__(self, other):
        return self.value/other

a = User(10)
